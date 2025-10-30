from __future__ import annotations

from typing import List

from typing_extensions import TypedDict

from ..types import BaseModel
from .playersearchresult import PlayerSearchResult, PlayerSearchResultTypedDict


class PlayerSearchResponseTypedDict(TypedDict):
    players: List[PlayerSearchResultTypedDict]
    r"""Array of players matching search criteria"""
    term: str
    r"""Search term used"""


class PlayerSearchResponse(BaseModel):
    players: List[PlayerSearchResult]
    r"""Array of players matching search criteria"""

    term: str
    r"""Search term used"""
