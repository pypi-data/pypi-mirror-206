from datetime import datetime
from dataclasses import dataclass, asdict

from klu.common.models import BaseEngineModel


@dataclass
class Model(BaseEngineModel):
    guid: str
    provider: str
    model_name: str
    updated_at: datetime = datetime.utcnow()
    created_at: datetime = datetime.utcnow()

    @classmethod
    def _from_engine_format(cls, data: dict) -> "Model":
        return cls._create_instance(
            **{
                "updated_at": data.pop("updatedAt"),
                "created_at": data.pop("createdAt"),
            },
            **data,
        )

    def _to_engine_format(self) -> dict:
        base_dict = asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v is not None})

        base_dict.pop("updated_at", None)
        base_dict.pop("created_at", None)

        return base_dict
