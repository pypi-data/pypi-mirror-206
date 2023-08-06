from typing import List

import aiohttp
from aiohttp import ClientResponseError
from aiohttp.web_exceptions import HTTPNotFound

from klu.api.client import APIClient
from klu.action.models import Action
from klu.common.models import KluClientBase
from klu.application.constants import APPLICATION_ENDPOINT
from klu.application.errors import ApplicationNotFoundError
from klu.application.models import Application, UpdateApplicationData


class ApplicationsClient(KluClientBase):
    async def get(self, app_id: str) -> Application:
        """
        Retrieves app actions information based on the app GUID.

        Args:
            app_id (str): ID of an application to fetch.

        Returns: Application object
        """
        async with aiohttp.ClientSession() as session:
            client = APIClient(session, self.api_key)
            try:
                response = await client.get(APPLICATION_ENDPOINT, {"app": app_id})
            except (HTTPNotFound, ClientResponseError) as e:
                if e.status == 404:
                    raise ApplicationNotFoundError(app_id)

            return Application._from_engine_format(response)

    async def update(
        self,
        app_id: str,
        data: UpdateApplicationData,
    ) -> dict:
        """
        Update application metadata

        Args:
            app_id (str): ID of an application to fetch actions for.
            data (UpdateApplicationData): New application data.

        Returns: Dict with the message about successful application update
        """

        async with aiohttp.ClientSession() as session:
            client = APIClient(session, self.api_key)
            try:
                response = await client.post(
                    f"{APPLICATION_ENDPOINT}",
                    data._to_engine_dict_empty_removed(app_id),
                )
            except (HTTPNotFound, ClientResponseError) as e:
                if e.status == 404:
                    raise ApplicationNotFoundError(app_id)

            return {"message": response.get("message")}

    async def get_actions_for_app(self, app_id: str) -> List[Action]:
        """
        Retrieves app actions information based on the app GUID.

        Args:
            app_id (str): ID of an application to fetch actions for.

        Returns: An array of actions found by provided app id.
        """
        async with aiohttp.ClientSession() as session:
            client = APIClient(session, self.api_key)
            try:
                response = await client.get(f"{APPLICATION_ENDPOINT}/actions", {"app": app_id})
            except (HTTPNotFound, ClientResponseError) as e:
                if e.status == 404:
                    raise ApplicationNotFoundError(app_id)

            return [Action._from_engine_format(action) for action in response]
