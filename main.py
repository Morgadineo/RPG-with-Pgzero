import random

from core.constants import CELL_SIZE, FPS, TITLE
from core.utils import map_to_cell
from map.world import World
from entities.player import Player
from entities.enemy import Ghost
from systems.movement import try_move
from systems.combat import battle
from ui.hud import draw as draw_hud

###############################################################################
# GAME STATE
###############################################################################

mode = "game"

###############################################################################
# WORLD
###############################################################################

world = World()

WIDTH = world.width * CELL_SIZE
HEIGHT = world.height * CELL_SIZE

###############################################################################
# PLAYER
###############################################################################

player = Player()

###############################################################################
# ENEMIES
###############################################################################

enemies = []
enemy_cells = set()

for _ in range(5):
    for _ in range(20):
        x = random.randint(1, world.width - 2)
        y = random.randint(2, world.height - 2)

        if not world.is_wall((x, y)) and (x, y) not in enemy_cells:
            enemy_cells.add((x, y))
            enemies.append(Ghost((x * CELL_SIZE, y * CELL_SIZE), CELL_SIZE))
            break

###############################################################################
# DRAW
###############################################################################

def draw():
    if mode != "game":
        return

    screen.fill("#2f3542")

    # MAP
    world.draw()

    # PLAYER
    player.draw()

    # ENEMIES
    for enemy in enemies:
        enemy.draw()
        screen.draw.text(
            str(enemy.health),
            center=(enemy.x + 30, enemy.y - 10),
            color="white",
            fontsize=30
        )

    # HUD
    draw_hud(player, screen)

###############################################################################
# INPUT
###############################################################################

def on_key_down(key):
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
        (player.x + dx, player.y + dy),
        CELL_SIZE
    )

    for enemy in enemies:
        if enemy.coordinate == new_cell:
            battle(player, enemy)
            if enemy.health <= 0:
                enemies.remove(enemy)
            return

    try_move(player, dx, dy, world)

###############################################################################
# UPDATE
###############################################################################

def update(dt):
    pass

