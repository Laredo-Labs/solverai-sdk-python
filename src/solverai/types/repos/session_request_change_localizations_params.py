# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..vcs_provider import VcsProvider

__all__ = ["SessionRequestChangeLocalizationsParams"]


class SessionRequestChangeLocalizationsParams(TypedDict, total=False):
    provider: Required[VcsProvider]

    org: Required[str]

    repo: Required[str]

    instruction: Required[str]
