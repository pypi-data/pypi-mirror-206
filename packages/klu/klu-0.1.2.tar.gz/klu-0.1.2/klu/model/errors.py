class ModelsNotFoundError(Exception):
    model_id: int = None

    def __init__(self, datum_id):
        self.model_id = datum_id
        self.message = f"Models for current user were not found"
        super().__init__(self.message)


class UnknownModelProviderError(Exception):
    model_provider: int = None

    def __init__(self, model_provider):
        self.model_provider = model_provider
        self.message = (
            f"An unknown model provider {self.model_provider} was used. "
            "Supported providers are [OpenAI, HuggingFace, NLPCloud, GooseAI, AI21 & Anthropic]"
        )
        super().__init__(self.message)
