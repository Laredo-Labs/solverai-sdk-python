# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["RepoListResponse", "RepoListResponseItem"]


class RepoListResponseItem(BaseModel):
    org: str

    repo: str


RepoListResponse: TypeAlias = List[RepoListResponseItem]
