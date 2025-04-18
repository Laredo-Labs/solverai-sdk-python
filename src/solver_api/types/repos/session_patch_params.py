# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..vcs_provider import VcsProvider

__all__ = ["SessionPatchParams"]


class SessionPatchParams(TypedDict, total=False):
    provider: Required[VcsProvider]

    org: Required[str]

    repo: Required[str]

    context_lines: Annotated[int, PropertyInfo(alias="contextLines")]

    interhunk_lines: Annotated[int, PropertyInfo(alias="interhunkLines")]
