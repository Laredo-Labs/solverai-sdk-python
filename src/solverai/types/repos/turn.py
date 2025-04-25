# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Turn"]


class Turn(BaseModel):
    id: str

    idx: int

    instruction: str

    session_id: str = FieldInfo(alias="sessionId")

    start_commit: str = FieldInfo(alias="startCommit")

    status: Literal["pending", "running", "completed", "cancelled", "error"]

    end_commit: Optional[str] = FieldInfo(alias="endCommit", default=None)

    error: Optional[str] = None
