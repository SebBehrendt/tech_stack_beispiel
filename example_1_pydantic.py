import json

from pydantic import parse_obj_as

from src.models.hoist import Hoist
from src.models.station import STATION_UNION_TYPE


FILE_PATH = "examples/simple_example.json"


# Load data from JSON file
with open(FILE_PATH, "r") as file:
    data = json.load(file)


# parse hoist data with pydantic to pydantic models

hoists = [parse_obj_as(Hoist, hoist_data) for hoist_data in data["Hoists"]]

print(hoists)


# parse station data with pydantic to pydantic models

stations = [
    parse_obj_as(STATION_UNION_TYPE, station_data) for station_data in data["Stations"]
]

print(stations)

# access data of objects

station = stations.pop()
print(f"Station exmample with id {station.id} and type {station.type}")
