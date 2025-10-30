
from __future__ import annotations
from ..types import BaseModel
from ..utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing_extensions import Annotated, TypedDict


class GetGameMatchupRankingsRequestTypedDict(TypedDict):
    game_id: str
    r"""Game identifier (10-digit format YYYYMMDDNN)"""


class GetGameMatchupRankingsRequest(BaseModel):
    game_id: Annotated[
        str,
        pydantic.Field(alias="gameId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Game identifier (10-digit format YYYYMMDDNN)"""
