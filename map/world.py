from pgzero.actor import Actor
from core.constants import CELL_SIZE
from map.maps import map_2
from core.utils import resize_actor

TILES = {
    "0": "border",
    "1": "floor",
    "2": "floor_debris"
}

class World:
    def __init__(self):
        self.map = map_2
        self.width = len(self.map[0])
        self.height = len(self.map)

    def draw(self):
        for y, row in enumerate(self.map):
            for x, value in enumerate(row):

                if value == "-":
                    continue
                tile = Actor(TILES[value], topleft=(x * CELL_SIZE, y * CELL_SIZE))
                resize_actor(tile, CELL_SIZE)
                tile.draw()
                

    def is_wall(self, cell):
        x, y = cell
        return self.map[y][x] == "0"

