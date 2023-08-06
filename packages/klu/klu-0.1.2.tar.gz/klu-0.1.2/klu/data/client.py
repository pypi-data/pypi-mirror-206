from typing import List

import aiohttp
from aiohttp import ClientResponseError
from aiohttp.web_exceptions import HTTPNotFound

from klu.common.models import KluClientBase
from klu.data.constants import DATA_ENDPOINT
from klu.data.errors import DataNotFoundError
from klu.action.errors import ActionNotFoundError
from klu.data.models import DataBaseClass, Data, ActionData


class DataClient(KluClientBase):
    async def get(self, datum_id: str) -> Data:
        """
        Retrieves data information based on the data ID.

        Args:
            datum_id (str): ID of a datum object to fetch.

        Returns: An object
        """
        async with aiohttp.ClientSession() as session:
            client = self.get_client(session)
            try:
                response = await client.get(f"{DATA_ENDPOINT}/{datum_id}")
            except (HTTPNotFound, ClientResponseError) as e:
                if e.status == 404:
                    raise DataNotFoundError(datum_id)

            return Data._from_engine_format(response)

    async def update(self, datum_id: int, datum_data: DataBaseClass) -> dict:
        """
        Updated data information based on the data ID and provided payload.

        Args:
            datum_id (str): ID of a datum object to update.
            datum_data (DataBaseClass): datum data to update

        Returns: Dictionary with a 'message' key containing successful update message
        """
        async with aiohttp.ClientSession() as session:
            client = self.get_client(session)
            try:
                response = await client.post(f"{DATA_ENDPOINT}/{datum_id}", datum_data._to_engine_format())
            except (HTTPNotFound, ClientResponseError) as e:
                if e.status == 404:
                    raise DataNotFoundError(datum_id)

            return {"message": response.get("message")}

    async def get_data_for_action(self, action_guid: str) -> List[ActionData]:
        """
        Retrieves data information for an action.

        Args:
            action_guid (str): Guid of an action to fetch data for.

        Returns: An array of actions found by provided app id.
        """
        async with aiohttp.ClientSession() as session:
            client = self.get_client(session)
            try:
                response = await client.get(f"{DATA_ENDPOINT}", {"agent": action_guid})
            except (HTTPNotFound, ClientResponseError) as e:
                if e.status == 404:
                    raise ActionNotFoundError(action_guid)

            return [ActionData._from_engine_format(data) for data in response]
