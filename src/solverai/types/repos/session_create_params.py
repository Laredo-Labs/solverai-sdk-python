# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..vcs_provider import VcsProvider
from .session_visibility import SessionVisibility

__all__ = ["SessionCreateParams"]


class SessionCreateParams(TypedDict, total=False):
    provider: Required[VcsProvider]

    org: Required[str]

    user_branch_name: Required[Annotated[str, PropertyInfo(alias="userBranchName")]]

    description: str

    title: str

    visibility: SessionVisibility
