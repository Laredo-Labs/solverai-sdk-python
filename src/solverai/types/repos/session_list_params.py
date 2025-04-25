# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..vcs_provider import VcsProvider
from .session_status import SessionStatus

__all__ = ["SessionListParams"]


class SessionListParams(TypedDict, total=False):
    provider: Required[VcsProvider]

    org: Required[str]

    only_user_owned: Annotated[bool, PropertyInfo(alias="onlyUserOwned")]

    page_offset: Annotated[int, PropertyInfo(alias="pageOffset")]

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    sort_attribute: Annotated[Literal["created", "lastModified"], PropertyInfo(alias="sortAttribute")]

    sort_order: Annotated[Literal["ascending", "descending"], PropertyInfo(alias="sortOrder")]

    status_filter: Annotated[List[SessionStatus], PropertyInfo(alias="statusFilter")]

    title_filter: Annotated[str, PropertyInfo(alias="titleFilter")]
