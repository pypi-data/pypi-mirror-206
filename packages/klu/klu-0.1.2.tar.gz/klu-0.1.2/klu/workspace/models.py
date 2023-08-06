from uuid import UUID, uuid4
from dataclasses import dataclass, asdict

from klu.common.models import BaseEngineModel


@dataclass
class Workspace(BaseEngineModel):
    name: str
    created_by_id: str
    project_guid: UUID = uuid4()

    @classmethod
    def _from_engine_format(cls, data: dict) -> "Workspace":
        return cls._create_instance(
            **{
                "created_by_id": data.pop("createdById", None),
            },
            **data,
        )

    def _to_engine_format(self) -> dict:
        base_dict = asdict(self)

        return {
            "createdById": base_dict.pop("created_by_id", None),
            **base_dict,
        }
