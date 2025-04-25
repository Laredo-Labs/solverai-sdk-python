# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from ...vcs_provider import VcsProvider

__all__ = ["StatusStreamParams"]


class StatusStreamParams(TypedDict, total=False):
    provider: Required[VcsProvider]

    org: Required[str]

    session_filter: List[str]
    """session id to filter for"""
