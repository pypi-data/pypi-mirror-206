from typing import Optional
from datetime import datetime
from dataclasses import dataclass, asdict

from klu.common.models import BaseEngineModel
from klu.application.errors import InvalidUpdateAppParamsError


@dataclass
class UpdateApplicationData:
    """
    Model that defines data that can be updated on an existing application object.
    At least one parameter should be passed

    Args:
        name (int): New name of the application.
        app_type (str): New app_type of the application.
        description (str): New description of the application.
    """

    name: Optional[str] = None
    app_type: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self):
        if not self.name and not self.app_type and not self.description:
            raise InvalidUpdateAppParamsError()

    def _to_engine_dict_empty_removed(self, app_id: str) -> dict:
        base_dict = asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v is not None})

        return {"app": app_id, **base_dict}


@dataclass
class Application(BaseEngineModel):
    id: str
    guid: str
    name: str
    app_type: str
    enabled: bool

    workspace_id: int
    created_by_id: str

    description: Optional[str]
    model_config: Optional[dict]
    deleted: Optional[bool] = None
    updated_at: Optional[datetime] = None
    created_at: datetime = datetime.utcnow()

    @classmethod
    def _from_engine_format(cls, data: dict) -> "Application":
        return cls._create_instance(
            **{
                "updated_at": data.pop("updatedAt"),
                "created_at": data.pop("createdAt"),
                "workspace_id": data.pop("workspaceId"),
                "created_by_id": data.pop("createdById"),
            },
            **data,
        )

    def _to_engine_format(self) -> dict:
        base_dict = asdict(self)

        return {
            "updatedAt": base_dict.pop("updated_at"),
            "createdAt": base_dict.pop("created_at"),
            "workspaceId": base_dict.pop("workspace_id"),
            "createdById": base_dict.pop("created_by_id"),
            **base_dict,
        }
