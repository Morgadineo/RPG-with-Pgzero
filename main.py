import random

from pgzero.builtins import keyboard
import pgzero.screen

from core.constants import CELL_SIZE, FPS, TITLE

from map.world import World

from entities.player import Player
from entities.enemy import Ghost

from ui.hud import draw as draw_hud

# Supress 'screen not defined' errors
screen : pgzero.screen.Screen

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

FPS = FPS

TITLE = TITLE

###############################################################################
# PLAYER
###############################################################################

player = Player(world.player_spawn_pos)

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

    player.movement(keyboard, enemies, world)

###############################################################################
# UPDATE
###############################################################################

def update(dt):
    pass

