from typing import List

import aiohttp
from aiohttp import ClientResponseError
from aiohttp.web_exceptions import HTTPNotFound

from klu.api.client import APIClient
from klu.workspace.models import Workspace
from klu.common.models import KluClientBase
from klu.data_index.models import DataIndex
from klu.application.models import Application
from klu.workspace.errors import WorkspaceOrUserNotFoundError
from klu.workspace.constants import (
    WORKSPACE_APPS_ENDPOINT,
    WORKSPACE_INDICES_ENDPOINT,
    WORKSPACE_ENDPOINT,
    SINGLE_WORKSPACE_ENDPOINT,
)


class WorkspaceClient(KluClientBase):
    async def get(self, workspace_guid: str) -> Workspace:
        """
        Retrieves a single workspace object by provided workspace_guid

        Args:
            workspace_guid (str): The ID of workspace to fetch.

        Returns: A workspace object
        """
        raise NotImplementedError(
            "This endpoint will be available in a newer version of the API"
        )
        # async with aiohttp.ClientSession() as session:
        # client = APIClient(session, self.api_key)
        # try:
        #     response = await client.get(
        #         SINGLE_WORKSPACE_ENDPOINT.format(workspace_guid=workspace_guid),
        #     )
        # except (HTTPNotFound, ClientResponseError) as e:
        #     if e.status == 404:
        #         raise WorkspaceOrUserNotFoundError()
        #
        # return Workspace._from_engine_format(response)

    async def list(self) -> List[Workspace]:
        """
        Retrieves the list of workspaces for currently authenticated user.

        Returns: Array of workspaces found for user
        """
        raise NotImplementedError(
            "This endpoint will be available in a newer version of the API"
        )
        # async with aiohttp.ClientSession() as session:
        # client = APIClient(session, self.api_key)
        # try:
        #     response = await client.get(WORKSPACE_ENDPOINT)
        # except (HTTPNotFound, ClientResponseError) as e:
        #     if e.status == 404:
        #         raise WorkspaceOrUserNotFoundError()
        #
        # return [Workspace._from_engine_format(workspace) for workspace in response]

    async def get_workspace_apps(self, workspace_guid: str) -> List[Application]:
        """
        Retrieves the list of applications for workspace defined by provided guid

        Args:
            workspace_guid (str): The ID of workspace to fetch applications for.

        Returns: List of applications found in a workspace
        """
        async with aiohttp.ClientSession() as session:
            client = APIClient(session, self.api_key)
            try:
                response = await client.get(
                    WORKSPACE_APPS_ENDPOINT.format(workspace_guid=workspace_guid),
                )
            except (HTTPNotFound, ClientResponseError) as e:
                if e.status == 404:
                    raise WorkspaceOrUserNotFoundError()

            return [
                Application._from_engine_format(application) for application in response
            ]

    async def get_workspace_indices(self, workspace_guid: str) -> List[DataIndex]:
        """
        Retrieves the list of applications for workspace defined by provided guid

        Args:
            workspace_guid (str): The ID of workspace to fetch applications for.

        Returns: List of DataIndex objects found on a workspace.
        """
        async with aiohttp.ClientSession() as session:
            client = APIClient(session, self.api_key)
            try:
                response = await client.get(
                    WORKSPACE_INDICES_ENDPOINT.format(workspace_guid=workspace_guid),
                )
            except (HTTPNotFound, ClientResponseError) as e:
                if e.status == 404:
                    raise WorkspaceOrUserNotFoundError()

            return [
                DataIndex._from_engine_format(data_index) for data_index in response
            ]
