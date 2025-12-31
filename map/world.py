from pgzero.actor import Actor
from core.constants import CELL_SIZE
from map.maps import get_map
from core.utils import resize_actor
from map.tile import TILES

class World:
    def __init__(self):
        self.map = get_map("first_floor")
        self.width = len(self.map[0])
        self.height = len(self.map)

    def draw(self):
        for y, row in enumerate(self.map):
            for x, value in enumerate(row):

                if value == "-":
                    continue

                tile = self.get_tile_object(value)

                tile.topleft = (x * CELL_SIZE, y * CELL_SIZE)
                
                resize_actor(tile, CELL_SIZE)

                tile.draw()
                
    def get_tile_object(self, id: str):
        tile = TILES[id]

        return tile

    def is_wall(self, cell: tuple[int, int]):
        x, y = cell

        tile = self.map[y][x]

        tile = self.get_tile_object(tile)

        return not tile.walkable

    def map_to_cell(self, pos: tuple[int, int], cell_size: int):
        return int(pos[0] / cell_size), int(pos[1] / cell_size)

    def cell_to_px(self, cell, cell_size):
        return cell[0] * cell_size, cell[1] * cell_size

