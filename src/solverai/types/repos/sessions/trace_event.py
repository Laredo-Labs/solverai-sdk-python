# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TraceEvent"]


class TraceEvent(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    has_patch: bool = FieldInfo(alias="hasPatch")

    idx: int

    turn_id: str = FieldInfo(alias="turnId")

    event_data: Optional[Dict[str, Union[str, bool, float]]] = FieldInfo(alias="eventData", default=None)
