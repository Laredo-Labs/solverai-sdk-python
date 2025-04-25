# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel
from ..session_status import SessionStatus
from ..session_visibility import SessionVisibility

__all__ = ["StatusStreamResponse", "ChangeData"]


class ChangeData(BaseModel):
    new_visibility: Optional[SessionVisibility] = None


class StatusStreamResponse(BaseModel):
    org: str

    repo: str

    session_id: str

    type: Literal["state_transition", "session_updated", "session_created", "session_deleted", "visibility_changed"]

    change_data: Optional[ChangeData] = None
    """Additional data about the change. Only present for `visibility_changed` events."""

    new_state: Optional[SessionStatus] = None
