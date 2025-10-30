
from __future__ import annotations
from .seasontypeenum import SeasonTypeEnum
from .sortorderenum import SortOrderEnum
from ..types import BaseModel
from ..utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


GetTeamDefenseRushStatsBySeasonSortKey = Literal[
    "total",
    "run",
    "runPct",
    "rushTd",
    "rushYds",
    "rushYpp",
    "epaRush",
    "epaRushPP",
    "rush10PYds",
    "stuffPct",
    "ryoe",
    "ryoeAtt",
    "ybcoAtt",
    "yacoAtt",
    "inPct",
    "outPct",
    "lightPct",
    "stackedPct",
    "rushYpg",
]
r"""Field to sort by"""


class GetTeamDefenseRushStatsBySeasonRequestTypedDict(TypedDict):
    season: int
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of season"""
    limit: NotRequired[int]
    r"""Maximum number of teams to return"""
    offset: NotRequired[int]
    r"""Number of records to skip for pagination"""
    page: NotRequired[int]
    r"""Page number for pagination"""
    sort_key: NotRequired[GetTeamDefenseRushStatsBySeasonSortKey]
    r"""Field to sort by"""
    sort_value: NotRequired[SortOrderEnum]
    r"""Sort direction"""


class GetTeamDefenseRushStatsBySeasonRequest(BaseModel):
    season: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Season year"""

    season_type: Annotated[
        SeasonTypeEnum,
        pydantic.Field(alias="seasonType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Type of season"""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 35
    r"""Maximum number of teams to return"""

    offset: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 0
    r"""Number of records to skip for pagination"""

    page: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 1
    r"""Page number for pagination"""

    sort_key: Annotated[
        Optional[GetTeamDefenseRushStatsBySeasonSortKey],
        pydantic.Field(alias="sortKey"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "rushYpg"
    r"""Field to sort by"""

    sort_value: Annotated[
        Optional[SortOrderEnum],
        pydantic.Field(alias="sortValue"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Sort direction"""
