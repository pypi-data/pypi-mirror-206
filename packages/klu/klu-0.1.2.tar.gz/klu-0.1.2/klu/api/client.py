from functools import wraps

import aiohttp

from typing import List, Union

from aiohttp import ClientResponseError
from aiohttp.web_exceptions import HTTPNotFound

from klu.common.errors import (
    UnknownKluError,
    UnauthorizedError,
    BadRequestAPIError,
    UnknownKluAPIError,
)
from klu.api.constants import API_ENDPOINT


def _handle_http_exception(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except (HTTPNotFound, ClientResponseError) as e:
            if e.status == 400:
                raise BadRequestAPIError(e.status, e.message)
            if e.status == 500:
                raise UnknownKluAPIError(e.status, e.message)
            if e.status == 401:
                raise UnauthorizedError()

            # Passing higher for more specific handling up to the functions level.
            raise e
        except Exception:
            raise UnknownKluError()

    return wrapper


class APIClient:
    def __init__(self, session: aiohttp.ClientSession, api_key: str):
        self.session = session
        self.headers = {"Authorization": f"Bearer {api_key}"}

    @_handle_http_exception
    async def get(self, path: str, params: dict = None) -> Union[dict, List[dict]]:
        url = f"{API_ENDPOINT}{path}"
        async with self.session.get(
            url, params=params, headers=self.headers
        ) as response:
            response.raise_for_status()
            return await response.json()

    @_handle_http_exception
    async def post(self, path: str, json_data: dict) -> dict:
        url = f"{API_ENDPOINT}{path}"
        async with self.session.post(
            url, json=json_data, headers=self.headers
        ) as response:
            response.raise_for_status()
            return await response.json()

    @_handle_http_exception
    async def put(self, path: str, json_data: dict) -> dict:
        url = f"{API_ENDPOINT}{path}"
        async with self.session.put(
            url, json=json_data, headers=self.headers
        ) as response:
            response.raise_for_status()
            return await response.json()

    @_handle_http_exception
    async def delete(self, path: str) -> dict:
        url = f"{API_ENDPOINT}{path}"
        async with self.session.delete(url, headers=self.headers) as response:
            response.raise_for_status()
            return await response.json()
