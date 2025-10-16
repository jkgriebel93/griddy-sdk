from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from .seasontypeenum import SeasonTypeEnum
from .sortorderenum import SortOrderEnum
from .teamdefensestats import TeamDefenseStats, TeamDefenseStatsTypedDict


class TeamDefenseStatsResponseTypedDict(TypedDict):
    defense: List[TeamDefenseStatsTypedDict]
    limit: int
    r"""Maximum number of results returned"""
    offset: int
    r"""Number of records skipped"""
    season: int
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of NFL season"""
    sort_key: str
    r"""Field used for sorting"""
    sort_value: SortOrderEnum
    r"""Sort direction for ordered results"""
    total: int
    r"""Total number of teams matching the criteria"""
    split: NotRequired[List[str]]
    r"""Applied defensive situation splits"""


class TeamDefenseStatsResponse(BaseModel):
    defense: List[TeamDefenseStats]

    limit: int
    r"""Maximum number of results returned"""

    offset: int
    r"""Number of records skipped"""

    season: int
    r"""Season year"""

    season_type: Annotated[SeasonTypeEnum, pydantic.Field(alias="seasonType")]
    r"""Type of NFL season"""

    sort_key: Annotated[str, pydantic.Field(alias="sortKey")]
    r"""Field used for sorting"""

    sort_value: Annotated[SortOrderEnum, pydantic.Field(alias="sortValue")]
    r"""Sort direction for ordered results"""

    total: int
    r"""Total number of teams matching the criteria"""

    split: Optional[List[str]] = None
    r"""Applied defensive situation splits"""
