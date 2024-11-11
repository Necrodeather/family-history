from typing import Any

from pydantic import BaseModel, ConfigDict


class BaseEntity(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def from_list(cls, obj: Any) -> list[BaseModel]:
        return [cls.model_validate(item) for item in obj]
