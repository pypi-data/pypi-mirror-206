from typing import Optional

import aiohttp
from aiohttp import ClientResponseError
from aiohttp.web_exceptions import HTTPNotFound

from klu.api.client import APIClient
from klu.data_index.constants import (
    DATA_INDEX_ENDPOINT,
    DATA_INDEX_STATUS_ENDPOINT,
    PROCESS_DATA_INDEX_ENDPOINT,
    UPLOAD_PRE_SIGNED_URL_ENDPOINT,
)
from klu.common.models import KluClientBase
from klu.data_index.errors import DataIndexNotFoundError
from klu.utils.file_upload import upload_to_pre_signed_url
from klu.workspace.errors import WorkspaceOrUserNotFoundError
from klu.common.errors import UnknownKluAPIError, UnknownKluError
from klu.data_index.models import DataIndexStatusEnum, PreSignUrlPostData, FileData


class DataIndexClient(KluClientBase):
    async def create(
        self,
        name: str,
        description: str,
        splitter: Optional[str] = None,
        file_data: Optional[FileData] = None,
    ) -> dict:
        """
        Creates a new index based on the provided data.

        Args:
            name (str): The name of the index
            description (str): The description of the index
            file_data (Optional[FileData]): Metadata of the file to be uploaded.
                Can be omitted if only the data_index skeleton has to be created
            splitter (Optional[str]): The column splitter - filter by the user when they are dealing with a multi
                tenanted environment.

        Returns: dict with a message about successful index creation and id of a newly created index file.
        Use this id to check the status of dataIndex processing.
        """
        file_url = await self.upload_index_file(file_data) if file_data else None
        async with aiohttp.ClientSession() as session:
            client = APIClient(session, self.api_key)
            try:
                data = {
                    "index_name": name,
                    "splitter": splitter,
                    "description": description,
                }
                if file_url:
                    data["file_url"] = file_url

                response = await client.post(DATA_INDEX_ENDPOINT, data)
            except (HTTPNotFound, ClientResponseError) as e:
                if e.status == 404:
                    raise WorkspaceOrUserNotFoundError()

                raise UnknownKluAPIError(e.status, e.message)
            except Exception:
                raise UnknownKluError()

            return {"message": response.get("msg"), "id": response.get("id")}

    async def get_status(self, data_index_id: str) -> DataIndexStatusEnum:
        """
        Retrieves the status of an index creation task based on the provided index ID.

        Args:
            data_index_id (str): The ID of the data index.

        Returns: string representing te data_index status
        """
        async with aiohttp.ClientSession() as session:
            client = APIClient(session, self.api_key)
            try:
                response = await client.post(
                    DATA_INDEX_STATUS_ENDPOINT,
                    {
                        "indexId": data_index_id,
                    },
                )
            except (HTTPNotFound, ClientResponseError) as e:
                if e.status == 404:
                    raise DataIndexNotFoundError(data_index_id)

            return DataIndexStatusEnum.get(response.get("status"))

    async def process_data_index(
        self, data_index_id: str, splitter: Optional[str] = None
    ) -> dict:
        """
        Processes existing index identified by provided daata_index id using provider column splitter

        Args:
            data_index_id (str): Id of data index to process
            splitter (Optional[str]): The column splitter - filter by the user when they are dealing with a multi
            tenanted environment.

        Returns: dict with a message about successful index creation
        """
        async with aiohttp.ClientSession() as session:
            client = APIClient(session, self.api_key)
            try:
                response = await client.post(
                    PROCESS_DATA_INDEX_ENDPOINT,
                    {
                        "splitter": splitter,
                        "indexId": data_index_id,
                    },
                )
            except (HTTPNotFound, ClientResponseError) as e:
                # TODO differentiate between missing data_index and missing user 404. Change the engine accordingly
                if e.status == 404:
                    raise WorkspaceOrUserNotFoundError()

                raise UnknownKluAPIError(e.status, e.message)
            except Exception:
                raise UnknownKluError()

            return {"message": response.get("msg")}

    async def upload_index_file(self, file_data: FileData) -> str:
        """
        Upload system file to Klu storage for later usage in data_index creation. Maximum supported file size is 50 MB.

        Args:
            file_data (FileData): Metadata of the file to be uploaded. For more details, see the FileData class docs.

        Returns: URL to the uploaded file. This URL should be used during the data_index creation flow.
        """
        async with aiohttp.ClientSession() as session:
            pre_signed_url_data = await self.get_index_upload_pre_signed_url(
                file_data.file_name
            )
            await upload_to_pre_signed_url(
                session, pre_signed_url_data, file_data.file_path
            )

            return pre_signed_url_data.object_url

    async def get_index_upload_pre_signed_url(
        self, file_name: str
    ) -> PreSignUrlPostData:
        """
        Get pre-signed url to upload files to use for data_indexes creation. Maximum supported file size is 50 MB.
        This method should only be used if you don't want to use `upload_model_file` function to upload the file without
        the need to get into pre_signed_url upload flow.

        Args:
            file_name (str): The name of the file to be uploaded. Has to be unique among the files you uploaded before.
            Otherwise, the new file will override the previously uploaded one by the same file_name

        Returns: pre-signed url data including url, which is the pre-signed url that can be used to upload the file.
            Also includes 'fields' property that contains dict with data that
            has to be passed alongside the file during the upload
            And object_url property that contains the url that can be used to access the file location after the upload.
            This same object_url can be used during the data_index creation.
            For a usage example check out the `upload_index_file` function
        """
        async with aiohttp.ClientSession() as session:
            client = APIClient(session, self.api_key)
            try:
                response = await client.post(
                    UPLOAD_PRE_SIGNED_URL_ENDPOINT,
                    {
                        "file_name": file_name,
                    },
                )
            except (HTTPNotFound, ClientResponseError) as e:
                # TODO differentiate between missing data_index and missing user 404. Change the engine accordingly
                if e.status == 404:
                    raise WorkspaceOrUserNotFoundError()

                raise UnknownKluAPIError(e.status, e.message)

            return PreSignUrlPostData(**response)
