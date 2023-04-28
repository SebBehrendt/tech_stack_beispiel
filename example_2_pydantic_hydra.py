import json

from pydantic import parse_obj_as

import hydra
from omegaconf import DictConfig


from src.models.hoist import Hoist
from src.models.station import STATION_UNION_TYPE


@hydra.main(version_base=None, config_path="conf", config_name="config")
def example_app(cfg: DictConfig) -> None:

    print("\n######### Config values #########")
    print("\ngeneral:")
    print(cfg["general"])

    print("\nproduction system:")
    print(cfg["production_system"])

    print("\nRL:")
    print(cfg["RL"])

    print("\nneural_network: ")
    print(cfg["neural_network"])
    
    
    file_path = cfg["production_system"]["file_path"]

    # Load data from JSON file
    with open(file_path, "r") as file:
        data = json.load(file)


    # parse hoist data with pydantic to pydantic models

    hoists = [parse_obj_as(Hoist, hoist_data) for hoist_data in data["Hoists"]]

    print("\nHoists:\n", hoists)


    # parse station data with pydantic to pydantic models

    stations = [
        parse_obj_as(STATION_UNION_TYPE, station_data) for station_data in data["Stations"]
    ]

    print("\nStations:\n", stations)


if __name__ == "__main__":
    example_app()