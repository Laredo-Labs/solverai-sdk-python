# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["EventPatchResponse"]


class EventPatchResponse(BaseModel):
    patch_set: Optional[str] = FieldInfo(alias="patchSet", default=None)
