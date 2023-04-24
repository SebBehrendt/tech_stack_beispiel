import json
import typing

from pydantic import parse_obj_as

import hydra
from omegaconf import DictConfig

from fastapi import FastAPI
import uvicorn


from src.models.hoist import Hoist
from src.models.station import STATION_UNION_TYPE

HOISTS: typing.List[Hoist] = []
STATIONS: typing.List[STATION_UNION_TYPE] = []

def load_data(cfg: DictConfig) -> typing.Tuple[Hoist, STATION_UNION_TYPE]:
    file_path = cfg["production_system"]["file_path"]
    with open(file_path, "r") as file:
        data = json.load(file)
    hoists = [parse_obj_as(Hoist, hoist_data) for hoist_data in data["Hoists"]]
    stations = [
        parse_obj_as(STATION_UNION_TYPE, station_data) for station_data in data["Stations"]
    ]
    return hoists, stations

def add_data_to_database(hoists: typing.List[Hoist], stations: typing.List[STATION_UNION_TYPE]):
    [HOISTS.append(hoist) for hoist in hoists]
    [STATIONS.append(station) for station in stations]

app = FastAPI(
    title="Example Server",
    description="Framework for RL in Galvanics",
    version="0.0.1a"
)

@app.get("/", response_model=str)
async def root():
    return "Example Server is running!"

@app.get("/hoists", response_model=typing.List[Hoist])
async def get_hoists():
    return HOISTS

@app.get("/stations", response_model=typing.List[STATION_UNION_TYPE])
async def get_stations():
    return STATIONS

@hydra.main(version_base=None, config_path="conf", config_name="config")
def example_app(cfg: DictConfig) -> None:
    hoists, stations = load_data(cfg)
    add_data_to_database(hoists, stations)
    uvicorn.run(app, host=cfg["general"]["url"], port=cfg["general"]["port"])
    

if __name__ == "__main__":
    example_app()