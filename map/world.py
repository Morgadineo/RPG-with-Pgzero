from map.tile import *
from core.constants import CELL_SIZE
from map.maps import get_map
from core.utils import resize_actor

class World:
    def __init__(self):
        self.map = get_map("first_floor")
        self.width = len(self.map[0])
        self.height = len(self.map)

        self.tiles = []
        self.player_spawn_pos = None

        self._build_world()

    def _build_world(self):
        for y, row in enumerate(self.map):
            for x, tile_id in enumerate(row):

                tile = self._create_tile(tile_id)

                tile.topleft = self.cell_to_px((x, y), CELL_SIZE)

                resize_actor(tile, CELL_SIZE)

                self.tiles.append(tile)

                ###################################
                # Found SpawnDoor and set only one!
                if isinstance(tile, SpawnDoor) and self.player_spawn_pos is None:
                    self.player_spawn_pos = (
                        tile.x,
                        tile.y
                    )
                ###################################

    def draw(self):
        for tile in self.tiles:
            tile.draw()

    def _create_tile(self, tile_id: str):
        base = TILES[tile_id]
        return base.__class__(base.id, base.name)

    def is_wall(self, cell: tuple[int, int]):
        x, y = cell
        tile_id = self.map[y][x]
        tile = TILES[tile_id]
        return not tile.walkable

    def map_to_cell(self, pos: tuple[int, int], cell_size: int):
        return int(pos[0] / cell_size), int(pos[1] / cell_size)

    def cell_to_px(self, cell, cell_size):
        return cell[0] * cell_size, cell[1] * cell_size

