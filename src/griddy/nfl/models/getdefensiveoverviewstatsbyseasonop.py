from __future__ import annotations

from typing import List, Literal, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from ..utils import FieldMetadata, QueryParamMetadata
from .seasontypeenum import SeasonTypeEnum
from .sortorderenum import SortOrderEnum

GetDefensiveOverviewStatsBySeasonSortKey = Literal[
    "snap",
    "rd",
    "pr",
    "tck",
    "tStop",
    "hStop",
    "qbp",
    "qbpR",
    "sack",
    "tgtNd",
    "recNd",
    "recYdsNd",
    "recTdNd",
    "int",
    "passRatingNd",
    "gameSnap",
    "snapPct",
]
r"""Field to sort by"""


class GetDefensiveOverviewStatsBySeasonRequestTypedDict(TypedDict):
    season: int
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of season"""
    limit: NotRequired[int]
    r"""Maximum number of players to return"""
    offset: NotRequired[int]
    r"""Number of records to skip for pagination"""
    page: NotRequired[int]
    r"""Page number for pagination"""
    sort_key: NotRequired[GetDefensiveOverviewStatsBySeasonSortKey]
    r"""Field to sort by"""
    sort_value: NotRequired[SortOrderEnum]
    r"""Sort direction"""
    qualified_defender: NotRequired[bool]
    r"""Filter to only qualified defenders (minimum snap threshold)"""
    team_defense: NotRequired[List[str]]
    r"""Filter by specific team IDs (supports multiple teams)"""


class GetDefensiveOverviewStatsBySeasonRequest(BaseModel):
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
    r"""Maximum number of players to return"""

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
        Optional[GetDefensiveOverviewStatsBySeasonSortKey],
        pydantic.Field(alias="sortKey"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "snap"
    r"""Field to sort by"""

    sort_value: Annotated[
        Optional[SortOrderEnum],
        pydantic.Field(alias="sortValue"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Sort direction"""

    qualified_defender: Annotated[
        Optional[bool],
        pydantic.Field(alias="qualifiedDefender"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Filter to only qualified defenders (minimum snap threshold)"""

    team_defense: Annotated[
        Optional[List[str]],
        pydantic.Field(alias="teamDefense"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by specific team IDs (supports multiple teams)"""
