import typing
from enum import Enum, auto
from pydantic import BaseModel


# example for a Station
        # {
        #     id: 23,
        #     type: ACTIVE_ZINC,
        #     line: 1,
        #     w_coeff: 0.5,
        #     alternatives: [19, 20, 21, 22]
        # }

class StationTypeEnum(str, Enum):
    LOAD_UNLOAD = "LOAD_UNLOAD"
    DUMMY = "DUMMY"
    DRYING = "DRYING"
    CLEANING = "CLEANING"
    BLUE = "BLUE"
    PICKLING = "PICKLING"
    ELECTRODEGREASING = "ELECTRODEGREASING"
    DEOXIDATION = "DEOXIDATION"
    ACTIVE_ZINC = "ACTIVE_ZINC"

class Station(BaseModel):
    id: int
    type: StationTypeEnum
    line: int
    w_coeff: float

    # class Config:
    #     use_enum_values = True

    class Config:
        extra="forbid"

class RedundantStation(Station):
    alternatives: typing.List[int]

STATION_UNION_TYPE = Station | RedundantStation
# STATION_UNION_TYPE = typing.Union[Station, RedundantStation]