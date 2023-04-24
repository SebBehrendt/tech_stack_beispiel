from pydantic import BaseModel, conlist


# example for a Hoist
# {
#                 id: 1,
#                 line: 1,
#                 transverser: false,
#                 travel_range: [1, 13],
#                 ini_station: 3,
#                 num_actions: 170
#             },

class Hoist(BaseModel):
    id: int
    line: int
    transverser: bool
    travel_range: conlist(item_type=int, min_items=2, max_items=2)
    ini_station: int
    num_actions: int
