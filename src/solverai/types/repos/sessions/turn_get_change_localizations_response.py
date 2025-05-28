# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["TurnGetChangeLocalizationsResponse", "File", "FileExcerpt"]


class FileExcerpt(BaseModel):
    content: str

    line_end: int

    line_start: int


class File(BaseModel):
    path: str

    excerpts: Optional[List[FileExcerpt]] = None

    relevance: Optional[str] = None

    score: Optional[float] = None


class TurnGetChangeLocalizationsResponse(BaseModel):
    files: List[File]
