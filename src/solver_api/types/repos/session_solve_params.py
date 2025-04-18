# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..vcs_provider import VcsProvider

__all__ = ["SessionSolveParams"]


class SessionSolveParams(TypedDict, total=False):
    provider: Required[VcsProvider]

    org: Required[str]

    repo: Required[str]

    instruction: Required[str]

    num_steps: Required[Annotated[int, PropertyInfo(alias="numSteps")]]
    """The maximum number of steps to take when Solving"""

    invocation_options: Annotated[Dict[str, Union[str, bool, float]], PropertyInfo(alias="invocationOptions")]
