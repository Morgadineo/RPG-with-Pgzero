import random

from pgzero.builtins import keyboard
import pgzero.screen

from core.constants import CELL_SIZE, FPS, TITLE
from map.world import World
from entities.player import Player
from entities.enemy import Enemy, Ghost
from systems.combat_scene import CombatScene
from ui.hud import draw as draw_hud

# Supress 'screen not defined' errors
screen: pgzero.screen.Screen

###############################################################################
# GAME STATE
###############################################################################

GAME_STATE_WORLD = "world"
GAME_STATE_BATTLE = "battle"

game_state = GAME_STATE_WORLD
combat_scene = None

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
    screen.clear()

    if game_state == GAME_STATE_WORLD:
        screen.fill("#2f3542")

        world.draw()
        player.draw()

        for enemy in enemies:
            enemy.draw()
            screen.draw.text(
                str(enemy.health),
                center=(enemy.x + 30, enemy.y - 10),
                color="white",
                fontsize=30
            )

        draw_hud(player, screen)

    elif game_state == GAME_STATE_BATTLE:
        world.draw()
        combat_scene.draw(screen)

###############################################################################
# INPUT
###############################################################################

def on_key_down(key):
    global game_state, combat_scene

    if game_state == GAME_STATE_WORLD:
        result = player.movement(keyboard, enemies, world)

        if isinstance(result, Enemy):
            game_state = GAME_STATE_BATTLE
            combat_scene = CombatScene(
                player,
                result,
                (WIDTH, HEIGHT)
            )

    elif game_state == GAME_STATE_BATTLE:
        combat_scene.on_key_down(keyboard)

###############################################################################
# UPDATE
###############################################################################

def update(dt):
    global game_state, combat_scene

    if game_state == GAME_STATE_BATTLE:
        combat_scene.update(dt)

        if combat_scene.finished:
            if combat_scene.winner == "player":
                enemies.remove(combat_scene.enemy)

            game_state = GAME_STATE_WORLD
            combat_scene = None

        return

    # WORLD UPDATE
    if len(enemies) == 0:
        world.change_map()
        player.spawn()
        enemy_cells.clear()

        for _ in range(5):
            for _ in range(20):
                x = random.randint(1, world.width - 2)
                y = random.randint(2, world.height - 2)

                if not world.is_wall((x, y)) and (x, y) not in enemy_cells:
                    enemy_cells.add((x, y))
                    enemies.append(Ghost((x * CELL_SIZE, y * CELL_SIZE), CELL_SIZE))
                    break

