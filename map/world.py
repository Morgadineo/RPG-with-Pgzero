from map.tile import *
from core.constants import CELL_SIZE
from map.maps import get_map, maps_list
from core.utils import resize_actor
from pytmx import TiledTileLayer

class World:
    def __init__(self):
        self.map_list = maps_list
        self.map_name = "first_floor"
        self.tmx = get_map(self.map_name)

        self.width = self.tmx.width
        self.height = self.tmx.height

        self.tiles: list = []
        self.player_spawn_pos = None

        self._build_world()

    def change_map(self):
        map_index = self.map_list.index(self.map_name)

        if map_index == len(self.map_list) - 1:
            map_index = 0

        else:
            map_index += 1

        self.map_name = self.map_list[map_index]
        self.tmx = get_map(self.map_name)
        self._build_world()

    def _build_world(self):
        for layer in self.tmx.visible_layers:

            # Ignora camadas que não são de tiles
            if not isinstance(layer, TiledTileLayer):
                continue

            for y in range(layer.height):
                for x in range(layer.width):
                    gid = layer.data[y][x]

                    if gid == 0:
                        continue

                    tile_props = self.tmx.get_tile_properties_by_gid(gid)
                    tile_image = self.tmx.get_tile_image_by_gid(gid)

                    tile = self._create_tile(tile_props, tile_image)

                    if tile is None:
                        continue

                    tile.topleft = self.cell_to_px((x, y), CELL_SIZE)

                    resize_actor(tile, CELL_SIZE)

                    self.tiles.append(tile)

                    ###################################
                    # SpawnDoor detection
                    if (
                        isinstance(tile, SpawnDoor)
                        and self.player_spawn_pos is None
                    ):
                        self.player_spawn_pos = (tile.topleft)
                    ###################################

    def draw(self):
        for tile in self.tiles:
            tile.draw()

    def _create_tile(self, props: dict | None, tile_image):
        """
        Cria o tile a partir das propriedades do Tiled
        """

        if props is None:
            return

        tile_id = props.get("id")
        tile_type = props.get("Type")

        if tile_type == "SpawnDoor":
            return SpawnDoor(tile_id, tile_image)

        if tile_type == "Wall":
            return Wall(tile_id, tile_image)

        if tile_type == "Floor":
            return Floor(tile_id, tile_image)

        # fallback
        return Floor(tile_id, tile_image)

    def is_wall(self, cell: tuple[int, int]):
        x, y = cell

        for layer in self.tmx.visible_layers:
            if not isinstance(layer, TiledTileLayer):
                continue

            gid = layer.data[y][x]
            if gid == 0:
                continue

            props = self.tmx.get_tile_properties_by_gid(gid)

            if props and props.get("Type") == "Wall":
                return True

        return False

    def map_to_cell(self, pos: tuple[int, int], cell_size: int):
        return int(pos[0] / cell_size), int(pos[1] / cell_size)

    def cell_to_px(self, cell, cell_size):
        return cell[0] * cell_size, cell[1] * cell_size

