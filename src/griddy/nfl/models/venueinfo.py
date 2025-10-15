from __future__ import annotations
from ..types import BaseModel
import pydantic
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


VenueInfoRoofType = Literal[
    "OUTDOOR",
    "DOME",
    "RETRACTABLE",
]


class VenueInfoTypedDict(TypedDict):
    postal_code: NotRequired[str]
    roof_type: NotRequired[VenueInfoRoofType]
    site_city: NotRequired[str]
    site_full_name: NotRequired[str]
    site_id: NotRequired[int]
    site_state: NotRequired[str]
    smart_id: NotRequired[str]


class VenueInfo(BaseModel):
    postal_code: Annotated[Optional[str], pydantic.Field(alias="postalCode")] = None

    roof_type: Annotated[
        Optional[VenueInfoRoofType], pydantic.Field(alias="roofType")
    ] = None

    site_city: Annotated[Optional[str], pydantic.Field(alias="siteCity")] = None

    site_full_name: Annotated[Optional[str], pydantic.Field(alias="siteFullName")] = (
        None
    )

    site_id: Annotated[Optional[int], pydantic.Field(alias="siteId")] = None

    site_state: Annotated[Optional[str], pydantic.Field(alias="siteState")] = None

    smart_id: Annotated[Optional[str], pydantic.Field(alias="smartId")] = None
