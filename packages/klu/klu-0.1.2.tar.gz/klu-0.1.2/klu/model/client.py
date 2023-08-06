from typing import List

import aiohttp

from aiohttp import ClientResponseError
from aiohttp.web_exceptions import HTTPNotFound

from klu.model.models import Model
from klu.common.models import KluClientBase
from klu.model.constants import MODEL_ENDPOINT
from klu.model.errors import UnknownModelProviderError
from klu.workspace.errors import WorkspaceOrUserNotFoundError


class ModelsClient(KluClientBase):
    async def list(self) -> List[Model]:
        """
        Retrieves the list of models for authenticated user

        Returns: An array of model objects with 'provider' and 'model_name' parameters in each object.
        """
        async with aiohttp.ClientSession() as session:
            client = self.get_client(session)
            try:
                response = await client.get(MODEL_ENDPOINT)
            except (HTTPNotFound, ClientResponseError) as e:
                if e.status == 404:
                    raise WorkspaceOrUserNotFoundError()

            return [Model._from_engine_format(model) for model in response]

    async def create(self, key: str, provider: str, model_name: str) -> dict:
        """
        Creates a model based on the data provided.

        Args:
            key (str): Model key. Required
            model_name (str): Model name. Required
            provider (str): Model provider. Required. Should be one of the following: [OpenAI, HuggingFace, NLPCloud, GooseAI, AI21 & Anthropic]

        Returns: A JSON response with a message about successful creation if model was created.
        """
        async with aiohttp.ClientSession() as session:
            client = self.get_client(session)
            try:
                response = await client.post(
                    MODEL_ENDPOINT,
                    {
                        "key": key,
                        "provider": provider,
                        "model_name": model_name,
                    },
                )
            except (HTTPNotFound, ClientResponseError) as e:
                # TODO differentiate between missing model and missing user 404.
                if e.status == 404:
                    raise WorkspaceOrUserNotFoundError()

            return {"message": response.get("message")}

    async def validate_provider_api_key(self, api_key: str, provider: str) -> bool:
        """
        Validates API keys for provided api_key and provider values.

        Args:
            api_key (str): Model api_key
            provider (str): Model provider. Required. Should be one of the following: [OpenAI, HuggingFace, NLPCloud, GooseAI, AI21 & Anthropic]

        Returns: A JSON response with a message about successful creation if model was created.
        """
        async with aiohttp.ClientSession() as session:
            client = self.get_client(session)
            try:
                response = await client.post(
                    MODEL_ENDPOINT,
                    {
                        "api_key": api_key,
                        "provider": provider,
                    },
                )
            except (HTTPNotFound, ClientResponseError) as e:
                if e.status == 404:
                    raise UnknownModelProviderError(provider)

            return bool(response.get("validated"))
