from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..types import BaseModel
from ..utils import FieldMetadata, QueryParamMetadata


class GetScheduleSeasonWeeksRequestTypedDict(TypedDict):
    season: int
    r"""Season year"""


class GetScheduleSeasonWeeksRequest(BaseModel):
    season: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Season year"""
