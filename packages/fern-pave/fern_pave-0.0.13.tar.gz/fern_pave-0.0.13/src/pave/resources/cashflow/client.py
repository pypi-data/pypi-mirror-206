# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from ...environment import PaveEnvironment
from .types.get_financial_health_response import GetFinancialHealthResponse
from .types.get_recurring_expenditures_response import GetRecurringExpendituresResponse


class CashflowClient:
    def __init__(self, *, environment: PaveEnvironment = PaveEnvironment.PRODUCTION, api_key: str):
        self._environment = environment
        self.api_key = api_key

    def get_financial_health(
        self, user_id: str, *, start_date: dt.date, end_date: dt.date, with_transactions: typing.Optional[bool] = None
    ) -> GetFinancialHealthResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"v1/users/{user_id}/financial_health"),
            params={
                "start_date": str(start_date),
                "end_date": str(end_date),
                "with_transactions": jsonable_encoder(with_transactions),
            },
            headers=remove_none_from_headers({"X-API-KEY": self.api_key}),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetFinancialHealthResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_recurring_expenditures(
        self, user_id: str, *, start_date: dt.date, end_date: dt.date, with_transactions: bool
    ) -> GetRecurringExpendituresResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"v1/users/{user_id}/recurring_expenditures"),
            params={"start_date": str(start_date), "end_date": str(end_date), "with_transactions": with_transactions},
            headers=remove_none_from_headers({"X-API-KEY": self.api_key}),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetRecurringExpendituresResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncCashflowClient:
    def __init__(self, *, environment: PaveEnvironment = PaveEnvironment.PRODUCTION, api_key: str):
        self._environment = environment
        self.api_key = api_key

    async def get_financial_health(
        self, user_id: str, *, start_date: dt.date, end_date: dt.date, with_transactions: typing.Optional[bool] = None
    ) -> GetFinancialHealthResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"v1/users/{user_id}/financial_health"),
                params={
                    "start_date": str(start_date),
                    "end_date": str(end_date),
                    "with_transactions": jsonable_encoder(with_transactions),
                },
                headers=remove_none_from_headers({"X-API-KEY": self.api_key}),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetFinancialHealthResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_recurring_expenditures(
        self, user_id: str, *, start_date: dt.date, end_date: dt.date, with_transactions: bool
    ) -> GetRecurringExpendituresResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"v1/users/{user_id}/recurring_expenditures"),
                params={
                    "start_date": str(start_date),
                    "end_date": str(end_date),
                    "with_transactions": with_transactions,
                },
                headers=remove_none_from_headers({"X-API-KEY": self.api_key}),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetRecurringExpendituresResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
