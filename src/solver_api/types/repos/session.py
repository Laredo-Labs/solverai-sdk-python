# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..vcs_provider import VcsProvider
from .session_status import SessionStatus
from .session_visibility import SessionVisibility

__all__ = ["Session"]


class Session(BaseModel):
    id: str

    base_revision: str = FieldInfo(alias="baseRevision")

    created: datetime

    last_modified: datetime = FieldInfo(alias="lastModified")

    org: str

    provider: VcsProvider

    repo: str

    status: SessionStatus

    title: str

    user_avatar_url: str = FieldInfo(alias="userAvatarUrl")

    user_branch_name: str = FieldInfo(alias="userBranchName")

    user_id: str = FieldInfo(alias="userId")

    user_name: str = FieldInfo(alias="userName")

    description: Optional[str] = None

    visibility: Optional[SessionVisibility] = None
