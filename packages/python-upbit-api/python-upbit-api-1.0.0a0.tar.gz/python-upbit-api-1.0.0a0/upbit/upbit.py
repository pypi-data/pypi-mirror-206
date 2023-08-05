from __future__ import annotations

import datetime
import functools
import hashlib
import logging
import re
import uuid
from typing import Any, Optional, Literal, Dict, Callable, Tuple
from urllib.parse import urlencode, unquote

import jwt
import requests
from requests import Response
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from upbit.exceptions import (
    _ERROR_EXCEPTION_DICT,
    TooManyRequests,
    UpbitServerError,
    UpbitError,
    UpbitClientError,
    ApiKeyError,
    RemainingReqValueError,
)

# 잔여 요청 그룹
RequestGroup = Literal[
    # Exchange API
    'default',  # 주문요청 외
    'order',
    # Quotation API
    'market', 'candles', 'ticker', 'crix-trades', 'orderbook',
]


class RemainingReq:
    """
    잔여 요청수 클래스
    참고) https://docs.upbit.com/docs/user-request-guide

    group: RequestGroup 잔여 요청 그룹명
    minute: 그룹별 분당 남은 요청수.
    second: 그룹별 초당 남은 요청수.
    updated: 요청수 응답을 저장한 일시.
    """

    def __init__(self, remaining_req: str):
        self._remaining_req = remaining_req

        pattern = re.compile(r"group=([a-z\-]+); min=([0-9]+); sec=([0-9]+)")
        matched = pattern.search(remaining_req)

        self.group: RequestGroup = matched.group(1)
        self.minute: int = int(matched.group(2))
        self.second: int = int(matched.group(3))
        self.updated: datetime.datetime = datetime.datetime.now()

    def __str__(self):
        return f"RemainingReq group={self.group!r}; min={self.minute!r}; sec={self.second!r}; updated={self.updated!r}"

    def __repr__(self):
        return f"RemainingReq(${self._remaining_req!r})"


class Upbit:
    def __init__(self,
                 access_key: str | None = None,
                 secret_key: str | None = None,
                 *,
                 timeout: float | Tuple[float, float] | None = (6, 30),
                 ):
        """

        :param access_key: 업비트 API Access Key
            Quotation API만 사용한다면 설정하지 않아도 됩니다.
            Exchange API를 사용하려면 필수로 설정해야 합니다.
            설정하지 않고 관련 메소드를 요청하면 ApiKeyError 예외가 발생합니다.

        :param secret_key: 업비트 API Secret Key
            Quotation API만 사용한다면 설정하지 않아도 됩니다.
            Exchange API를 사용하려면 필수로 설정해야 합니다.
            설정하지 않고 관련 메소드를 요청하면 ApiKeyError 예외가 발생합니다.

        :param timeout: 업비트 API request 의 기본 timeout 설정값. (connect, read)
            예) connect, read timeout 함께 설정시 timeout=5
            예) connect, read timeout 따로 설정시 timeout=(6, 12)
            예) None 인 경우 무한 대기
            업비트 서버 점검시 연결 되지 않으며 커넥션이 무한 대기 상태가 됩니다. 이를 방지를 위해 적절한 timout 값을 설정하길 권장합니다.
            참고: https://requests.readthedocs.io/en/latest/user/advanced/#timeouts
        """

        self._endpoint = "https://api.upbit.com/v1"

        self._access_key = access_key
        self._secret_key = secret_key

        # 요청 그룹별 잔여 요청수를 저장할 딕셔너리
        # - 키: group 명 / 값: RemainingReq 인스턴스
        self._remaining_reqs: Dict[RequestGroup, RemainingReq] = {}

        # 서버에러시 자동으로 재시도하도록 max_retries 설정
        self._session = requests.Session()
        # https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html#module-urllib3.util.retry
        retry = Retry(
            total=None,
            # 각자 설정해야 Retry 발생시 로그에서 어떤 요인인지 쉽게 알 수 있음.
            redirect=5,
            status=5,
            connect=0,
            read=0,
            other=0,
            backoff_factor=1,
            # 기본값에 post 추가
            allowed_methods=frozenset({'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PUT', 'TRACE', 'POST'}),
            # 서버 에러 - todo check 429 추가?
            status_forcelist=tuple(range(500, 512)),
            raise_on_status=True,
        )
        self._session.mount(self._endpoint, HTTPAdapter(max_retries=retry))
        self._session.request = functools.partial(self._session.request, timeout=timeout)

        self._logger = logging.getLogger(__name__)

    def _request_wrapper(func: Callable):
        """
        업비트 API 요청 래퍼

        1) 잔여 요청수 처리
        2) HTTPError를 UpbitError로 변환
        """

        def wrapper(self, *args: Any, **kwargs: Dict[str, Any]) -> Response:
            remaining_req: Optional[RemainingReq] = None

            try:
                response: Response = func(self, *args, **kwargs)

                # 잔여 요청수 기록
                remaining_req = self._process_remaining_req(response.headers.get("Remaining-Req"))

                # status code가 400~600 일 때 예외 발생시키기
                response.raise_for_status()

                return response
            except requests.HTTPError as e:
                status_code = e.response.status_code

                # TooManyRequests 에러 처리
                if status_code == requests.codes.too_many_requests:
                    # 이 에러는 규격화된 Upbit 에러 JSON 바디를 갖지 않음.
                    raise TooManyRequests(f"Upbit TooManyRequests Error {status_code} Remaining-Req={remaining_req}", e)

                # Upbit API 주요 에러 코드 목록에 명시된 에러 처리
                elif status_code in [400, 401]:
                    try:
                        # 에러 코드와 맞는 예외를 찾아 발생시킨다.
                        error_body = e.response.json()["error"]
                        error_code = error_body.get("name")
                        error_msg = error_body.get("message")
                        error_exception = _ERROR_EXCEPTION_DICT.get(error_code)
                        if error_exception:
                            raise error_exception(f"Upbit Client Error {status_code} {error_code=!r} {error_msg=!r}", e)
                    except requests.JSONDecodeError:
                        raise UpbitClientError(f'Upbit Client Error {status_code} {e.response.reason}', e)

                # 기타 Upbit Client error 처리
                elif 400 <= status_code < 500:
                    raise UpbitClientError(f'Upbit Client Error {status_code} {e.response.reason}', e)

                # Upbit Server error 처리
                elif 500 <= self.status_code < 600:
                    raise UpbitServerError(f'Upbit Server Error {status_code} {e.response.reason}', e)

                # 방어적 에러 작성 - 발생하지 않아야 함.
                raise UpbitError(f'Upbit Error {status_code} {e.response.reason}', e)

        return wrapper

    @_request_wrapper
    def _request_get(self, url: str, **kwargs) -> Response:
        return self._session.get(url, **kwargs)

    @_request_wrapper
    def _request_put(self, url: str, **kwargs) -> Response:
        return self._session.put(url, **kwargs)

    @_request_wrapper
    def _request_post(self, url: str, **kwargs) -> Response:
        return self._session.post(url, **kwargs)

    @_request_wrapper
    def _request_delete(self, url: str, **kwargs) -> Response:
        return self._session.delete(url, **kwargs)

    def _process_remaining_req(self, remaining_req: str) -> Optional[RemainingReq]:
        """
        Remaining-Req 응답 헤더를 캐시하고 RemainingReq 인스턴스로 변환하여 반환한다.

        :param remaining_req: Remaining-Req 응답 헤더값
        :return: RemainingReq 인스턴스
        """
        try:
            rr = RemainingReq(remaining_req)
            self._remaining_reqs[rr.group] = rr
            self._logger.debug(f"Upbit API 잔여 요청수 {rr}")
            return rr
        except RemainingReqValueError as e:
            self._logger.warning(f"Upbit API 잔여 요청수 처리 RemainingReqValueError. {e!r}")
            pass
        except Exception as e:
            self._logger.warning(f"Upbit API 잔여 요청수 처리 에러. {remaining_req=!r} {e!r}")
            pass

    def _auth_guard(func: Callable):
        """인증이 필요한 메서드 호출시 API 키가 셋팅되어 있는지 확인하는 가드"""

        def wrapper(self, *args, **kwargs) -> Callable:
            if not self._access_key or not self._secret_key:
                raise ApiKeyError(f'{func.__name__} 메서드는 API Key 가 필요해요. '
                                  f'Upbit 인스턴스 생성시 access_key, secret_key 값을 인자로 넣어주세요.')

            return func(self, *args, **kwargs)

        return wrapper

    def _get_request_headers(self, query: Dict = None) -> Dict:
        payload = {
            "access_key": self._access_key,
            "nonce": str(uuid.uuid4())
        }

        if query is not None:
            query = {k: v for k, v in query.items() if v is not None}
            query_string = unquote(urlencode(query, doseq=True)).encode("utf-8")
            m = hashlib.sha512()
            m.update(query_string)
            query_hash = m.hexdigest()
            payload['query_hash'] = query_hash
            payload['query_hash_alg'] = "SHA512"

        jwt_token = jwt.encode(payload, self._secret_key)
        authorization_token = 'Bearer {}'.format(jwt_token)
        headers = {"Authorization": authorization_token}
        return headers

    def get_remaining_reqs(self, group: RequestGroup) -> Optional[RemainingReq]:
        """
        그룹의 잔여 요청수 정보 반환

        :param group: RequestGroup 잔여 요청 그룹
        :return: RemainingReq 잔여 요청 정보. 이전 응답 헤더에서 얻은 정보를 저장해 놓은 가장 최신 정보.
        """
        return self._remaining_reqs.get(group)

    # --------------------------------------------------------------------------
    # Exchange API > 자산
    # --------------------------------------------------------------------------

    @_auth_guard
    def get_accounts(self, **kwargs) -> Response:
        """
        전체 계좌 조회
        https://docs.upbit.com/reference/%EC%A0%84%EC%B2%B4-%EA%B3%84%EC%A2%8C-%EC%A1%B0%ED%9A%8C
        :return:
            data example:
            [{
                'currency': 'KRW',
                'balance': '628906.97823303',
                'locked': '0',
                'avg_buy_price': '0',
                'avg_buy_price_modified': True,
                'unit_currency': 'KRW'
            }, {
                'currency': 'ELF',
                'balance': '1142.57511675',
                'locked': '0',
                'avg_buy_price': '292.6613',
                'avg_buy_price_modified': False,
                'unit_currency': 'KRW'
            }, ...]
        """
        url = self._endpoint + "/accounts"
        headers = self._get_request_headers()

        return self._request_get(url, headers=headers, **kwargs)

    # --------------------------------------------------------------------------
    # Exchange API > 주문
    # --------------------------------------------------------------------------

    @_auth_guard
    def get_order_chance(self, market: str = "KRW-BTC", **kwargs) -> Response:
        """
        주문 가능 정보 조회
        https://docs.upbit.com/reference/%EC%A3%BC%EB%AC%B8-%EA%B0%80%EB%8A%A5-%EC%A0%95%EB%B3%B4
        :param market: 마켓 코드 (ex. KRW-BTC)
        :return:
            data example:
            {'ask_account': {'avg_buy_price': '28560783.8337',
                             'avg_buy_price_modified': False,
                             'balance': '0',
                             'currency': 'BTC',
                             'locked': '0',
                             'unit_currency': 'KRW'},
             'ask_fee': '0.0005',
             'bid_account': {'avg_buy_price': '0',
                             'avg_buy_price_modified': True,
                             'balance': '628906.97823303',
                             'currency': 'KRW',
                             'locked': '0',
                             'unit_currency': 'KRW'},
             'bid_fee': '0.0005',
             'maker_ask_fee': '0.0005',
             'maker_bid_fee': '0.0005',
             'market': {'ask': {'currency': 'BTC', 'min_total': '5000'},
                        'ask_types': ['limit', 'market'],
                        'bid': {'currency': 'KRW', 'min_total': '5000'},
                        'bid_types': ['limit', 'price'],
                        'id': 'KRW-BTC',
                        'max_total': '1000000000',
                        'name': 'BTC/KRW',
                        'order_sides': ['ask', 'bid'],
                        'order_types': ['limit'],
                        'state': 'active'}}
        """
        url = self._endpoint + "/orders/chance"
        params = {
            "market": market,
        }
        headers = self._get_request_headers(params)

        return self._request_get(url, headers=headers, params=params, **kwargs)

    @_auth_guard
    def get_order(self, order_uuid: str = None, identifier: str = None, **kwargs) -> Response:
        """
        개별 주문 조회
        https://docs.upbit.com/reference/%EA%B0%9C%EB%B3%84-%EC%A3%BC%EB%AC%B8-%EC%A1%B0%ED%9A%8C
        :param order_uuid: 주문 UUID
        :param identifier: 조회용 사용자 지정 값
        :return:
            data example:
            {
                'created_at': '2023-02-06T11:00:45+09:00',
                'executed_volume': '132.99843443',
                'locked': '0',
                'market': 'KRW-STRAX',
                'ord_type': 'market',
                'paid_fee': '50.738902735045',
                'remaining_fee': '0',
                'remaining_volume': '0',
                'reserved_fee': '0',
                'side': 'ask',
                'state': 'done',
                'trades': [{'created_at': '2023-02-06T11:00:44+09:00',
                         'funds': '101477.80547009',
                         'market': 'KRW-STRAX',
                         'price': '763',
                         'side': 'ask',
                         'trend': 'down',
                         'uuid': '3f818e33-e8be-495c-a62f-f7697735f2bd',
                         'volume': '132.99843443'}],
                'trades_count': 1,
                'uuid': 'd7c96420-a9ab-4ae8-a461-3db412427fb3',
                'volume': '132.99843443'
            }
        """
        url = self._endpoint + "/order"
        params = {
            "uuid": order_uuid,
            "identifier": identifier,
        }
        headers = self._get_request_headers(params)

        return self._request_get(url, headers=headers, params=params, **kwargs)

    @_auth_guard
    def get_orders(self, market: str = None, uuids: [str] = None, identifiers: [str] = None,
                   state: str = 'wait', states: [str] = None, page: int = 1, limit: int = 100,
                   order_by: str = 'desc', **kwargs) -> Response:
        """
        주문 리스트 조회
        https://docs.upbit.com/reference/%EC%A3%BC%EB%AC%B8-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%A1%B0%ED%9A%8C
        :param market: 마켓 아이디
        :param uuids: 주문 UUID의 목록
        :param identifiers: 주문 identifier의 목록
        :param state: 주문 상태 wait, watch, done, cancel
        :param states: 주문 상태의 목록
        :param page: 페이지 수, default: 1
        :param limit: 요청 개수, default: 100
        :param order_by: 정렬 방식 asc, desc(default)
        :return:
            data example:
            [{
                'created_at': '2023-02-15T08:00:40+09:00',
                'executed_volume': '380.4181703',
                'locked': '0',
                'market': 'KRW-ELF',
                'ord_type': 'market',
                'paid_fee': '56.6823073747',
                'remaining_fee': '0',
                'remaining_volume': '0',
                'reserved_fee': '0',
                'side': 'ask',
                'state': 'done',
                'trades_count': 1,
                'uuid': 'd5c96aeb-b519-46a8-bb79-f694e40acc71',
                'volume': '380.4181703'
            }, ...]
        """
        url = self._endpoint + "/orders"
        params = {
            "market": market,
            "uuids[]": uuids,
            "identifiers[]": identifiers,
            "state": state,
            "states[]": states,
            "page": page,
            "limit": limit,
            "order_by": order_by,
        }
        headers = self._get_request_headers(params)

        return self._request_get(url, headers=headers, params=params, **kwargs)

    @_auth_guard
    def delete_order(self, order_uuid: str = None, identifier: str = None, **kwargs) -> Response:
        """
        주문 취소 접수
        https://docs.upbit.com/reference/%EC%A3%BC%EB%AC%B8-%EC%B7%A8%EC%86%8C
        :param order_uuid: 주문 UUID
        :param identifier: 조회용 사용자 지정 값
        :return:
            data example:
            {
                "uuid": "cdd92199-2897-4e14-9448-f923320408ad",
                "side": "bid",
                "ord_type": "limit",
                "price": "100.0",
                "state": "wait",
                "market": "KRW-BTC",
                "created_at": "2018-04-10T15:42:23+09:00",
                "volume": "0.01",
                "remaining_volume": "0.01",
                "reserved_fee": "0.0015",
                "remaining_fee": "0.0015",
                "paid_fee": "0.0",
                "locked": "1.0015",
                "executed_volume": "0.0",
                "trades_count": 0
            }
        """
        url = self._endpoint + "/order"
        params = {
            "uuid": order_uuid,
            "identifier": identifier,
        }
        headers = self._get_request_headers(params)

        return self._request_delete(url, headers=headers, params=params, **kwargs)

    @_auth_guard
    def create_order(self, market: str, side: str, ord_type: str,
                     volume: str = None, price: str = None,
                     identifier: str = None, **kwargs) -> Response:
        """
        주문하기
        https://docs.upbit.com/reference/%EC%A3%BC%EB%AC%B8%ED%95%98%EA%B8%B0
        :param market: 마켓 ID (필수)
        :param side: 주문 종류 (필수) - bid(매수), ask(매도)
        :param ord_type: 주문 타입 (필수) - limit(지정가), price(시장가 매수), market(시장가 매도)
        :param volume: 주문량 (지정가, 시장가 매도 시 필수)
        :param price: 주문 가격. (지정가, 시장가 매수 시 필수)
        :param identifier: 조회용 사용자 지정 값 (선택)
        :return:
            data example:
            {
                "uuid": "cdd92199-2897-4e14-9448-f923320408ad",
                "side": "bid",
                "ord_type": "limit",
                "price": "100.0",
                "avg_price": "0.0",
                "state": "wait",
                "market": "KRW-BTC",
                "created_at": "2018-04-10T15:42:23+09:00",
                "volume": "0.01",
                "remaining_volume": "0.01",
                "reserved_fee": "0.0015",
                "remaining_fee": "0.0015",
                "paid_fee": "0.0",
                "locked": "1.0015",
                "executed_volume": "0.0",
                "trades_count": 0
            }
        """
        url = self._endpoint + "/orders"
        params = {
            "market": market,
            "side": side,
            "volume": volume,
            "price": price,
            "ord_type": ord_type,
            "identifier": identifier,
        }
        headers = self._get_request_headers(params)

        return self._request_post(url, headers=headers, params=params, **kwargs)

    # --------------------------------------------------------------------------
    # Exchange API > 출금
    # --------------------------------------------------------------------------

    @_auth_guard
    def get_withdraws(self, currency: str = None, state: str = None, uuids: [str] = None, txids: [str] = None,
                      page: int = 1, limit: int = 100, order_by: str = 'desc', **kwargs) -> Response:
        """
        출금 리스트 조회
        https://docs.upbit.com/reference/%EC%A0%84%EC%B2%B4-%EC%B6%9C%EA%B8%88-%EC%A1%B0%ED%9A%8C
        :param currency: Currency 코드
        :param state: 출금 상태 WAITING, PROCESSING, DONE, FAILED, CANCELLED, REJECTED
        :param uuids: 출금 UUID의 목록
        :param txids: 출금 TXID의 목록
        :param page: 페이지 수, default: 1
        :param limit: 개수 제한 (default: 100, max: 100)
        :param order_by: 정렬 방식 asc, desc(default)
        :return:
            data example:
            [{
                "type": "withdraw",
                "uuid": "35a4f1dc-1db5-4d6b-89b5-7ec137875956",
                "currency": "XRP",
                "txid": "98c15999f0bdc4ae0e8a-ed35868bb0c204fe6ec29e4058a3451e-88636d1040f4baddf943274ce37cf9cc",
                "state": "DONE",
                "created_at": "2019-02-28T15:17:51+09:00",
                "done_at": "2019-02-28T15:22:12+09:00",
                "amount": "1.00",
                "fee": "0.0",
                "transaction_type": "default"
            }, ...]
        """
        url = self._endpoint + "/withdraws"
        params = {
            "currency": currency,
            "state": state,
            "uuids[]": uuids,
            "txids[]": txids,
            "page": page,
            "limit": limit,
            "order_by": order_by,
        }
        headers = self._get_request_headers(params)

        return self._request_get(url, headers=headers, params=params, **kwargs)

    @_auth_guard
    def get_withdraw(self, data_uuid: str = None, txid: str = None, currency: str = None, **kwargs) -> Response:
        """
        개별 출금 조회
        https://docs.upbit.com/reference/%EA%B0%9C%EB%B3%84-%EC%B6%9C%EA%B8%88-%EC%A1%B0%ED%9A%8C
        :param data_uuid: 출금 UUID
        :param txid: 출금 TXID
        :param currency: Currency 코드
        :return:
            data example:
            {
                "type": "withdraw",
                "uuid": "9f432943-54e0-40b7-825f-b6fec8b42b79",
                "currency": "BTC",
                "txid": null,
                "state": "processing",
                "created_at": "2018-04-13T11:24:01+09:00",
                "done_at": null,
                "amount": "0.01",
                "fee": "0.0",
                "transaction_type": "default"
            }
        """
        url = self._endpoint + "/withdraw"
        params = {
            "uuid": data_uuid,
            "txid": txid,
            "currency": currency,
        }
        headers = self._get_request_headers(params)

        return self._request_get(url, headers=headers, params=params, **kwargs)

    @_auth_guard
    def get_withdraw_chance(self, currency: str, **kwargs) -> Response:
        """
        출금 가능 정보 조회
        https://docs.upbit.com/reference/%EC%B6%9C%EA%B8%88-%EA%B0%80%EB%8A%A5-%EC%A0%95%EB%B3%B4
        :param currency: Currency 코드
        :return:
            data example:
            {
                "member_level": {
                    "security_level": 3,
                    "fee_level": 0,
                    "email_verified": true,
                    "identity_auth_verified": true,
                    "bank_account_verified": true,
                    "kakao_pay_auth_verified": false,
                    "locked": false,
                    "wallet_locked": false
                },
                "currency": {
                    "code": "BTC",
                    "withdraw_fee": "0.0005",
                    "is_coin": true,
                    "wallet_state": "working",
                    "wallet_support": [
                      "deposit",
                      "withdraw"
                    ]
                },
                "account": {
                    "currency": "BTC",
                    "balance": "10.0",
                    "locked": "0.0",
                    "avg_buy_price": "8042000",
                    "avg_buy_price_modified": false,
                    "unit_currency": "KRW",
                },
                "withdraw_limit": {
                    "currency": "BTC",
                    "minimum": null,
                    "onetime": null,
                    "daily": "10.0",
                    "remaining_daily": "10.0",
                    "remaining_daily_krw": "0.0",
                    "fixed": null,
                    "can_withdraw": true
                }
            }
        """
        url = self._endpoint + "/withdraws/chance"
        params = {
            "currency": currency,
        }
        headers = self._get_request_headers(params)

        return self._request_get(url, headers=headers, params=params, **kwargs)

    @_auth_guard
    def create_withdraw_coin(self, currency: str, amount: float, address: str,
                             secondary_address: str = None, transaction_type: str = 'default',
                             **kwargs) -> Response:
        """
        코인 출금하기
        https://docs.upbit.com/reference/%EC%BD%94%EC%9D%B8-%EC%B6%9C%EA%B8%88%ED%95%98%EA%B8%B0
        :param currency: Currency 코드
        :param amount: 출금 수량
        :param address: 출금 가능 주소에 등록된 출금 주소
        :param secondary_address: 2차 출금 주소 (필요한 코인에 한해서)
        :param transaction_type: 출금 유형 - default : 일반출금, internal : 바로출금
        :return:
            data example:
            {
                "type": "withdraw",
                "uuid": "9f432943-54e0-40b7-825f-b6fec8b42b79",
                "currency": "BTC",
                "txid": "ebe6937b-130e-4066-8ac6-4b0e67f28adc",
                "state": "processing",
                "created_at": "2018-04-13T11:24:01+09:00",
                "done_at": null,
                "amount": "0.01",
                "fee": "0.0",
                "krw_amount": "80420.0",
                "transaction_type": "default"
            }
        """
        url = self._endpoint + "/withdraws/coin"
        params = {
            "currency": currency,
            "amount": amount,
            "address": address,
            "secondary_address": secondary_address,
            "transaction_type": transaction_type,
        }
        headers = self._get_request_headers(params)

        return self._request_post(url, headers=headers, json=params, **kwargs)

    @_auth_guard
    def create_withdraw_krw(self, amount: float, two_factor_type: str = 'kakao_pay', **kwargs) -> Response:
        """
        원화 출금하기
        https://docs.upbit.com/reference/%EC%9B%90%ED%99%94-%EC%B6%9C%EA%B8%88%ED%95%98%EA%B8%B0
        :param amount: 출금 수량
        :param two_factor_type: 2차 인증 수단 - kakao_pay : 카카오페이 인증(default), naver : 네이버 인증
        :return:
            data example:
            {
                "type": "withdraw",
                "uuid": "9f432943-54e0-40b7-825f-b6fec8b42b79",
                "currency": "KRW",
                "txid": "ebe6937b-130e-4066-8ac6-4b0e67f28adc",
                "state": "processing",
                "created_at": "2018-04-13T11:24:01+09:00",
                "done_at": null,
                "amount": "10000",
                "fee": "0.0",
                "transaction_type": "default"
            }
        """
        url = self._endpoint + "/withdraws/krw"
        params = {
            "amount": amount,
            "two_factor_type": two_factor_type,
        }
        headers = self._get_request_headers(params)

        return self._request_post(url, headers=headers, json=params, **kwargs)

    # --------------------------------------------------------------------------
    # Exchange API > 입금
    # --------------------------------------------------------------------------

    @_auth_guard
    def get_deposits(self, currency: str = None, state: str = None, uuids: [str] = None, txids: [str] = None,
                     page: int = 1, limit: int = 100, order_by: str = 'desc', **kwargs) -> Response:
        """
        입금 리스트 조회
        https://docs.upbit.com/reference/%EC%9E%85%EA%B8%88-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%A1%B0%ED%9A%8C
        :param currency: Currency 코드
        :param state: 출금 상태 WAITING, PROCESSING, DONE, FAILED, CANCELLED, REJECTED
        :param uuids: 출금 UUID의 목록
        :param txids: 출금 TXID의 목록
        :param page: 페이지 수, default: 1
        :param limit: 개수 제한 (default: 100, max: 100)
        :param order_by: 정렬 방식 asc, desc(default)
        :return:
            data example:
            [{
                "type": "deposit",
                "uuid": "94332e99-3a87-4a35-ad98-28b0c969f830",
                "currency": "KRW",
                "txid": "9e37c537-6849-4c8b-a134-57313f5dfc5a",
                "state": "ACCEPTED",
                "created_at": "2017-12-08T15:38:02+09:00",
                "done_at": "2017-12-08T15:38:02+09:00",
                "amount": "100000.0",
                "fee": "0.0",
                "transaction_type": "default"
            }, ...]
        """
        url = self._endpoint + "/deposits"
        params = {
            "currency": currency,
            "state": state,
            "uuids[]": uuids,
            "txids[]": txids,
            "page": page,
            "limit": limit,
            "order_by": order_by,
        }
        headers = self._get_request_headers(params)

        return self._request_get(url, headers=headers, params=params, **kwargs)

    @_auth_guard
    def get_deposit(self, data_uuid: str = None, txid: str = None, currency: str = None, **kwargs) -> Response:
        """
        개별 입금 조회
        https://docs.upbit.com/reference/%EA%B0%9C%EB%B3%84-%EC%9E%85%EA%B8%88-%EC%A1%B0%ED%9A%8C
        :param data_uuid: 출금 UUID
        :param txid: 출금 TXID
        :param currency: Currency 코드
        :return:
            data example:
            {
                "type": "deposit",
                "uuid": "94332e99-3a87-4a35-ad98-28b0c969f830",
                "currency": "KRW",
                "txid": "9e37c537-6849-4c8b-a134-57313f5dfc5a",
                "state": "ACCEPTED",
                "created_at": "2017-12-08T15:38:02+09:00",
                "done_at": "2017-12-08T15:38:02+09:00",
                "amount": "100000.0",
                "fee": "0.0",
                "transaction_type": "default"
            }
        """
        url = self._endpoint + "/deposit"
        params = {
            "uuid": data_uuid,
            "txid": txid,
            "currency": currency,
        }
        headers = self._get_request_headers(params)

        return self._request_get(url, headers=headers, params=params, **kwargs)

    @_auth_guard
    def create_deposit_krw(self, amount: float, two_factor_type: str = 'kakao_pay', **kwargs) -> Response:
        """
        원화 입금하기
        https://docs.upbit.com/reference/%EC%9B%90%ED%99%94-%EC%9E%85%EA%B8%88%ED%95%98%EA%B8%B0
        :param amount: 출금 수량
        :param two_factor_type: 2차 인증 수단 - kakao_pay : 카카오페이 인증(default), naver : 네이버 인증
        :return:
            data example:
            {
                "type": "deposit",
                "uuid": "9f432943-54e0-40b7-825f-b6fec8b42b79",
                "currency": "KRW",
                "txid": "ebe6937b-130e-4066-8ac6-4b0e67f28adc",
                "state": "processing",
                "created_at": "2018-04-13T11:24:01+09:00",
                "done_at": null,
                "amount": "10000",
                "fee": "0.0",
                "transaction_type": "default"
            }
        """
        url = self._endpoint + "/deposits/krw"
        params = {
            "amount": amount,
            "two_factor_type": two_factor_type,
        }
        headers = self._get_request_headers(params)

        return self._request_post(url, headers=headers, json=params, **kwargs)

    @_auth_guard
    def get_coin_addresses(self, **kwargs) -> Response:
        """
        전체 입금 주소 조회
        https://docs.upbit.com/reference/%EC%A0%84%EC%B2%B4-%EC%9E%85%EA%B8%88-%EC%A3%BC%EC%86%8C-%EC%A1%B0%ED%9A%8C
        :return:
            data example:
            [{
                "currency": "BTC",
                "deposit_address": "3EusRwybuZUhVDeHL7gh3HSLmbhLcy7NqD",
                "secondary_address": null
            }, ...]
        """
        url = self._endpoint + "/deposits/coin_addresses"
        headers = self._get_request_headers()

        return self._request_get(url, headers=headers, **kwargs)

    @_auth_guard
    def get_coin_address(self, currency: str = None, **kwargs) -> Response:
        """
        개별 입금 주소 조회
        https://docs.upbit.com/reference/%EA%B0%9C%EB%B3%84-%EC%9E%85%EA%B8%88-%EC%A3%BC%EC%86%8C-%EC%A1%B0%ED%9A%8C
        :param currency: Currency 코드
        :return:
            data example:
            {
                "currency": "BTC",
                "deposit_address": "3EusRwybuZUhVDeHL7gh3HSLmbhLcy7NqD",
                "secondary_address": null
            }
        """
        url = self._endpoint + "/deposits/coin_address"
        params = {
            "currency": currency,
        }
        headers = self._get_request_headers(params)

        return self._request_get(url, headers=headers, params=params, **kwargs)

    @_auth_guard
    def create_coin_address(self, currency: str, **kwargs) -> Response:
        """
        입금 주소 생성하기
        https://docs.upbit.com/reference/%EC%9E%85%EA%B8%88-%EC%A3%BC%EC%86%8C-%EC%83%9D%EC%84%B1-%EC%9A%94%EC%B2%AD
        :param currency: Currency 코드
        :return:
            data example:
            {
              "success": true,
              "message": "BTC 입금주소를 생성중입니다."
            }
        """
        url = self._endpoint + "/deposits/generate_coin_address"
        params = {
            "currency": currency,
        }
        headers = self._get_request_headers(params)

        return self._request_post(url, headers=headers, json=params, **kwargs)

    # --------------------------------------------------------------------------
    # Exchange API > 서비스 정보
    # --------------------------------------------------------------------------

    @_auth_guard
    def get_wallet_status(self, **kwargs) -> Response:
        """
        입출금 현황 조회 (전체)
        https://docs.upbit.com/reference/%EC%9E%85%EC%B6%9C%EA%B8%88-%ED%98%84%ED%99%A9
        :return:
            data example:
            [{
                'currency': 'BTC',
                'wallet_state': 'working',
                'block_state': 'normal',
                'block_height': 776512,
                'block_updated_at': '2023-02-14T13:37:39.806+00:00',
                'block_elapsed_minutes': 12
            }, ...]
        """
        url = self._endpoint + "/status/wallet"
        headers = self._get_request_headers()

        return self._request_get(url, headers=headers, **kwargs)

    @_auth_guard
    def get_api_keys(self, **kwargs) -> Response:
        """
        API 키 리스트 조회
        https://docs.upbit.com/reference/open-api-%ED%82%A4-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%A1%B0%ED%9A%8C
        :return:
            data example:
            [{'access_key': 'xxxxxxxxxxxxxxxxxxxxxxxx', 'expire_at': '2024-02-13T13:57:59+09:00'}, ...]
        """
        url = self._endpoint + "/api_keys"
        headers = self._get_request_headers()

        return self._request_get(url, headers=headers, **kwargs)

    # --------------------------------------------------------------------------
    # Quotation API > 시세 종목 조회
    # --------------------------------------------------------------------------

    def get_markets(self, is_detail: bool = None, **kwargs) -> Response:
        """
        거래 가능한 마켓 목록 조회
        https://docs.upbit.com/reference/%EB%A7%88%EC%BC%93-%EC%BD%94%EB%93%9C-%EC%A1%B0%ED%9A%8C
        :param is_detail: 유의 종목(market_warning) 정보 포함 여부
        :return:
            data example:
            [{
                'market_warning': 'NONE',
                'market': 'KRW-BTC',
                'korean_name': '비트코인',
                'english_name': 'Bitcoin'
            }, ...]
        """
        url = self._endpoint + "/market/all"
        params = {
            "isDetails": is_detail,
        }

        return self._request_get(url, params=params, **kwargs)

    # --------------------------------------------------------------------------
    # Quotation API > 시세 캔들 조회
    # --------------------------------------------------------------------------

    def get_candles_minute(self, unit: int = 1, market: str = "KRW-BTC",
                           to: str = None, count: int = None, **kwargs) -> Response:
        """
        분(Minute) 캔들 조회
        https://docs.upbit.com/reference/%EB%B6%84minute-%EC%BA%94%EB%93%A4-1
        :param unit: 분 단위. 가능한 값 : 1, 3, 5, 15, 10, 30, 60, 240
        :param market: 마켓 코드 (ex. KRW-BTC)
        :param to: 마지막 캔들 시각 (exclusive). 포맷 : yyyy-MM-dd'T'HH:mm:ss'Z' or yyyy-MM-dd HH:mm:ss. 비워서 요청시 가장 최근 캔들
        :param count: 캔들 개수(최대 200개까지 요청 가능) - 200개 초과로 요청해도 200개만 응답함
        :return:
            data example:
            [{
                'market': 'KRW-BTC',
                'candle_date_time_utc': '2023-02-14T09:43:00',
                'candle_date_time_kst': '2023-02-14T18:43:00',
                'opening_price': 28087000.0,
                'high_price': 28090000.0,
                'low_price': 28080000.0,
                'trade_price': 28090000.0,
                'timestamp': 1676367808940,
                'candle_acc_trade_price': 71066390.72097,
                'candle_acc_trade_volume': 2.53044043,
                'unit': 1
            }, ...]
        """
        url = self._endpoint + "/candles/minutes/" + str(unit)
        params = {
            "market": market,
            "to": to,
            "count": count,
        }

        return self._request_get(url, params=params, **kwargs)

    def get_candles_day(self, market: str = "KRW-BTC", to: str = None, count: int = None,
                        converting_price_unit: str = None, **kwargs) -> Response:
        """
        일(Day) 캔들 조회
        https://docs.upbit.com/reference/%EC%9D%BCday-%EC%BA%94%EB%93%A4-1
        :param market: 마켓 코드 (ex. KRW-BTC)
        :param to: 마지막 캔들 시각 (exclusive). 포맷 : yyyy-MM-dd'T'HH:mm:ss'Z' or yyyy-MM-dd HH:mm:ss. 비워서 요청시 가장 최근 캔들
        :param count: 캔들 개수(최대 200개까지 요청 가능) - 200개 초과로 요청해도 200개만 응답함
        :param converting_price_unit: 원화 마켓이 아닌 다른 마켓(ex. BTC, ETH)의 일봉 요청시, 종가 환산 화폐 단위 (예, KRW)
        :return:
            data example:
            [{
                'market': 'USDT-BTC',
                'candle_date_time_utc': '2023-02-14T00:00:00',
                'candle_date_time_kst': '2023-02-14T09:00:00',
                'opening_price': 21366.66292861,
                'high_price': 21977.99979999,
                'low_price': 21121.0004,
                'trade_price': 21873.26751835,
                'timestamp': 1676368771710,
                'candle_acc_trade_price': 147537.66926034,
                'candle_acc_trade_volume': 6.80355829,
                'prev_closing_price': 21366.46782971,
                'change_price': 506.79968864,
                'change_rate': 0.0237193949,
                'converted_trade_price': 28139000.000001043
            }, ...]
        """
        url = self._endpoint + "/candles/days"
        params = {
            "market": market,
            "to": to,
            "count": count,
            "convertingPriceUnit": converting_price_unit,
        }

        return self._request_get(url, params=params, **kwargs)

    def get_candles_week(self, market: str = "KRW-BTC", to: str = None, count: int = None, **kwargs) -> Response:
        """
        주(Week) 캔들 조회
        https://docs.upbit.com/reference/%EC%A3%BCweek-%EC%BA%94%EB%93%A4-1
        :param market: 마켓 코드 (ex. KRW-BTC)
        :param to: 마지막 캔들 시각 (exclusive). 포맷 : yyyy-MM-dd'T'HH:mm:ss'Z' or yyyy-MM-dd HH:mm:ss. 비워서 요청시 가장 최근 캔들
        :param count: 캔들 개수(최대 200개까지 요청 가능) - 200개 초과로 요청해도 200개만 응답함
        :return:
            data example:
            [{
                'market': 'KRW-BTC',
                'candle_date_time_utc': '2023-02-14T09:43:00',
                'candle_date_time_kst': '2023-02-14T18:43:00',
                'opening_price': 28087000.0,
                'high_price': 28090000.0,
                'low_price': 28080000.0,
                'trade_price': 28090000.0,
                'timestamp': 1676367808940,
                'candle_acc_trade_price': 71066390.72097,
                'candle_acc_trade_volume': 2.53044043,
                'first_day_of_period': '2023-02-13'
            }, ...]
        """
        url = self._endpoint + "/candles/weeks"
        params = {
            "market": market,
            "to": to,
            "count": count,
        }

        return self._request_get(url, params=params, **kwargs)

    def get_candles_month(self, market: str = "KRW-BTC", to: str = None, count: int = None, **kwargs) -> Response:
        """
        월(Month) 캔들 조회
        https://docs.upbit.com/reference/%EC%9B%94month-%EC%BA%94%EB%93%A4-1
        :param market: 마켓 코드 (ex. KRW-BTC)
        :param to: 마지막 캔들 시각 (exclusive). 포맷 : yyyy-MM-dd'T'HH:mm:ss'Z' or yyyy-MM-dd HH:mm:ss. 비워서 요청시 가장 최근 캔들
        :param count: 캔들 개수(최대 200개까지 요청 가능) - 200개 초과로 요청해도 200개만 응답함
        :return:
            data example:
            [{
                'market': 'KRW-BTC',
                'candle_date_time_utc': '2023-02-14T09:43:00',
                'candle_date_time_kst': '2023-02-14T18:43:00',
                'opening_price': 28087000.0,
                'high_price': 28090000.0,
                'low_price': 28080000.0,
                'trade_price': 28090000.0,
                'timestamp': 1676367808940,
                'candle_acc_trade_price': 71066390.72097,
                'candle_acc_trade_volume': 2.53044043,
                'first_day_of_period': '2023-02-01'
            }, ...]
        """
        url = self._endpoint + "/candles/months"
        params = {
            "market": market,
            "to": to,
            "count": count,
        }

        return self._request_get(url, params=params, **kwargs)

    # --------------------------------------------------------------------------
    # Quotation API > 시세 체결 조회
    # --------------------------------------------------------------------------

    def get_trades_ticks(self, market: str = "KRW-BTC", to: str = None, count: int = None,
                         cursor: str = None, days_ago: int = None, **kwargs) -> Response:
        """
        최근 체결 내역 조회
        https://docs.upbit.com/reference/%EC%B5%9C%EA%B7%BC-%EC%B2%B4%EA%B2%B0-%EB%82%B4%EC%97%AD
        :param market: 마켓 코드 (ex. KRW-BTC)
        :param to: 마지막 체결 시각. 형식 : [HHmmss 또는 HH:mm:ss]. 비워서 요청시 가장 최근 데이터
        :param count: 체결 개수. 최대 500개
        :param cursor: 페이지네이션 커서 (sequentialId)
        :param days_ago: 최근 체결 날짜 기준 7일 이내의 이전 데이터 조회 가능. 비워서 요청 시 가장 최근 체결 날짜 반환. (범위: 1 ~ 7))
        :return:
            data example:
            [{
                'market': 'KRW-BTC',
                'trade_date_utc': '2023-02-14',
                'trade_time_utc': '12:52:42',
                'timestamp': 1676379162028,
                'trade_price': 28250000.0,
                'trade_volume': 0.00353982,
                'prev_closing_price': 28309000.0,
                'change_price': -59000.0,
                'ask_bid': 'BID',
                'sequential_id': 1676379162028000
            }, ...]
        """
        url = self._endpoint + "/trades/ticks"
        params = {
            "market": market,
            "to": to,
            "count": count,
            "cursor": cursor,
            "daysAgo": days_ago,
        }

        return self._request_get(url, params=params, **kwargs)

    # --------------------------------------------------------------------------
    # Quotation API > 시세 현재가 조회
    # --------------------------------------------------------------------------

    def get_ticker(self, markets: [str] = None, **kwargs) -> Response:
        """
        현재가 정보 조회
        https://docs.upbit.com/reference/ticker%ED%98%84%EC%9E%AC%EA%B0%80-%EC%A0%95%EB%B3%B4
        :param markets: 마켓 코드 리스트 (ex. ["KRW-BTC"])
        :return:
            data example:
            [{
                'market': 'KRW-BTC',
                'trade_date': '20230214',
                'trade_time': '130155',
                'trade_date_kst': '20230214',
                'trade_time_kst': '220155',
                'trade_timestamp': 1676379715095,
                'opening_price': 28334000,
                'high_price': 28344000,
                'low_price': 28055000,
                'trade_price': 28256000,
                'prev_closing_price': 28309000.0,
                'change': 'FALL',
                'change_price': 53000.0,
                'change_rate': 0.0018721961,
                'signed_change_price': -53000.0,
                'signed_change_rate': -0.0018721961,
                'trade_volume': 0.01116417,
                'acc_trade_price': 101147638956.17886,
                'acc_trade_price_24h': 136755693662.07787,
                'acc_trade_volume': 3589.8072519,
                'acc_trade_volume_24h': 4856.21610445,
                'highest_52_week_price': 57678000.0,
                'highest_52_week_date': '2022-03-28',
                'lowest_52_week_price': 20700000.0,
                'lowest_52_week_date': '2022-12-30',
                'timestamp': 1676379715138
            }, ...]
        """
        if markets is None:
            markets = ["KRW-BTC"]

        url = self._endpoint + "/ticker"
        params = {
            "markets": markets,
        }

        return self._request_get(url, params=params, **kwargs)

    # --------------------------------------------------------------------------
    # Quotation API > 시세 호가 조회
    # --------------------------------------------------------------------------

    def get_orderbook(self, markets: [str] = None, **kwargs) -> Response:
        """
        호가 정보 조회
        https://docs.upbit.com/reference/%ED%98%B8%EA%B0%80-%EC%A0%95%EB%B3%B4-%EC%A1%B0%ED%9A%8C
        :param markets: 마켓 코드 리스트 (ex. ["KRW-BTC"])
        :return:
            data example:
            [{
                'market': 'KRW-BTC',
                'timestamp': 1676380537532,
                'total_ask_size': 5.71529774,
                'total_bid_size': 3.5650408600000008,
                'orderbook_units':
                    [{'ask_price': 28252000.0, 'bid_price': 28242000.0, 'ask_size': 0.22130992, 'bid_size': 0.69372092},
                    {'ask_price': 28253000.0, 'bid_price': 28241000.0, 'ask_size': 0.51485752, 'bid_size': 0.01781927},
                    {'ask_price': 28254000.0, 'bid_price': 28240000.0, 'ask_size': 1.23555378, 'bid_size': 0.93009378},
                    {'ask_price': 28255000.0, 'bid_price': 28239000.0, 'ask_size': 0.00473407, 'bid_size': 0.22},
                    {'ask_price': 28259000.0, 'bid_price': 28237000.0, 'ask_size': 0.49577839, 'bid_size': 0.00067571},
                    {'ask_price': 28261000.0, 'bid_price': 28233000.0, 'ask_size': 0.69107286, 'bid_size': 0.04437211},
                    {'ask_price': 28264000.0, 'bid_price': 28232000.0, 'ask_size': 0.01106274, 'bid_size': 0.18722972},
                    {'ask_price': 28265000.0, 'bid_price': 28231000.0, 'ask_size': 0.46430584, 'bid_size': 1.2079},
                    {'ask_price': 28266000.0, 'bid_price': 28230000.0, 'ask_size': 0.01860825, 'bid_size': 0.00318532},
                    {'ask_price': 28267000.0, 'bid_price': 28228000.0, 'ask_size': 0.02096061, 'bid_size': 0.01687993},
                    {'ask_price': 28268000.0, 'bid_price': 28227000.0, 'ask_size': 0.01, 'bid_size': 0.02220865},
                    {'ask_price': 28269000.0, 'bid_price': 28225000.0, 'ask_size': 0.0169, 'bid_size': 0.00035429},
                    {'ask_price': 28270000.0, 'bid_price': 28223000.0, 'ask_size': 0.02017691, 'bid_size': 0.02408774},
                    {'ask_price': 28271000.0, 'bid_price': 28222000.0, 'ask_size': 0.17979996, 'bid_size': 0.08573207},
                    {'ask_price': 28272000.0, 'bid_price': 28221000.0, 'ask_size': 1.81017689, 'bid_size': 0.11078135}
            }, ...]
        """
        if markets is None:
            markets = ["KRW-BTC"]

        url = self._endpoint + "/orderbook"
        params = {
            "markets": markets,
        }

        return self._request_get(url, params=params, **kwargs)
