import pytest

from unittest.mock import patch

from klu.client.klu import KluClient
from tests.utils.mock import APIClientMock


def mock_api_client():
    api_client_patch = patch("klu.api.client.APIClient", new=APIClientMock())
    api_client_patch.start()


@pytest.fixture(scope="function")
def klu_client() -> KluClient:
    return KluClient('test_api_key')


# We need it at global level to make sure APIClient is always mocked no matter which function is running
mock_api_client()
