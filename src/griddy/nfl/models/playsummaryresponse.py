
from __future__ import annotations
from .gameschedule import GameSchedule, GameScheduleTypedDict
from .playdetail import PlayDetail, PlayDetailTypedDict
from .playplayer import PlayPlayer, PlayPlayerTypedDict
from ..types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PlaySummaryResponseTypedDict(TypedDict):
    game_id: int
    r"""Game identifier in integer format"""
    play: PlayDetailTypedDict
    play_id: int
    r"""Play identifier"""
    schedule: GameScheduleTypedDict
    away: NotRequired[List[PlayPlayerTypedDict]]
    r"""Away team players involved in the play"""
    game_key: NotRequired[int]
    r"""Unique game key"""
    gsis_play_id: NotRequired[int]
    r"""GSIS play identifier"""
    home: NotRequired[List[PlayPlayerTypedDict]]
    r"""Home team players involved in the play"""
    home_is_offense: NotRequired[bool]
    r"""Whether home team has offensive possession"""


class PlaySummaryResponse(BaseModel):
    game_id: Annotated[int, pydantic.Field(alias="gameId")]
    r"""Game identifier in integer format"""

    play: PlayDetail

    play_id: Annotated[int, pydantic.Field(alias="playId")]
    r"""Play identifier"""

    schedule: GameSchedule

    away: Optional[List[PlayPlayer]] = None
    r"""Away team players involved in the play"""

    game_key: Annotated[Optional[int], pydantic.Field(alias="gameKey")] = None
    r"""Unique game key"""

    gsis_play_id: Annotated[Optional[int], pydantic.Field(alias="gsisPlayId")] = None
    r"""GSIS play identifier"""

    home: Optional[List[PlayPlayer]] = None
    r"""Home team players involved in the play"""

    home_is_offense: Annotated[
        Optional[bool], pydantic.Field(alias="homeIsOffense")
    ] = None
    r"""Whether home team has offensive possession"""
