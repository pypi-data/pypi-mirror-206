#!/usr/bin/env python
"""Tests for `action` module functions"""
import pytest

from aiohttp import web
from unittest.mock import patch

from klu.client.klu import KluClient
from klu.application.errors import ApplicationNotFoundError
from tests.application.utils import get_application_data
from tests.utils.mock import (
    get_api_client_mock,
    client_get_function_mock,
    get_return_value_side_effect,
)


@pytest.mark.asyncio
@patch("klu.application.client.APIClient", new_callable=get_api_client_mock)
async def test_get_app_converts_response_to_dataclass_provided_valid_response_dicts(
    client_mock, klu_client: KluClient
):
    test_app_guid = "test-guid"

    client_mock.get = client_get_function_mock(
        get_return_value_side_effect(get_application_data(guid=test_app_guid))
    )
    result = await klu_client.applications.get("test")

    assert result.guid == test_app_guid


@pytest.mark.asyncio
@patch("klu.application.client.APIClient", new_callable=get_api_client_mock)
async def test_get_app_raises_klu_error_provided_404_response_from_api(
    client_mock, klu_client: KluClient
):
    client_mock.get = client_get_function_mock(web.HTTPNotFound())
    with pytest.raises(Exception) as exc_info:
        await klu_client.applications.get_actions_for_app("test")

    assert exc_info.type is ApplicationNotFoundError
