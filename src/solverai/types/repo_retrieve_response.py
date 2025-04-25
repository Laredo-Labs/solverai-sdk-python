# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["RepoRetrieveResponse", "RepoRetrieveResponseItem"]


class RepoRetrieveResponseItem(BaseModel):
    org: str

    repo: str


RepoRetrieveResponse: TypeAlias = List[RepoRetrieveResponseItem]
