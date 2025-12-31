from pgzero.actor import Actor
from core.constants import CELL_SIZE
from core.utils import resize_actor, map_to_cell
from systems.combat import battle

class Player(Actor):
    def __init__(self):
        super().__init__('entities/player/player_stand', topleft=(CELL_SIZE, CELL_SIZE * 2))
        resize_actor(self, CELL_SIZE)

        self.health = 100
        self.attack = 5

    #TODO: [] Modularize movement function.
    def movement(self, keyboard, enemies, world):
        """
        Handle the player movement.
        
        Actualy this functions handle the keyboard input, enemy collision/battle when collided and the non walkable tile collision.

        Params:
            keyboard: The pgzero keyboard module;
            enemies: The list of enemies in the map;
            world: The world module.

        Return:
            None: If non movement is made. The player does not move if:
                      - A non movement key is pressed;
                      - The player collide with a enemy (battle initiate);
                      - The player collide with a non walkable tile.
        """
        dx = dy = 0

        if keyboard.right:
            dx = CELL_SIZE
        elif keyboard.left:
            dx = -CELL_SIZE
        elif keyboard.down:
            dy = CELL_SIZE
        elif keyboard.up:
            dy = -CELL_SIZE

        if dx == 0 and dy == 0:
            return

        new_cell = map_to_cell(
            (self.x + dx, self.y + dy),
            CELL_SIZE
        )

        for enemy in enemies:
            if enemy.coordinate == new_cell:
                battle(self, enemy)
                if enemy.health <= 0:
                    enemies.remove(enemy)
                return

        if world.is_wall(new_cell):
            return

        self.x += dx
        self.y += dy

