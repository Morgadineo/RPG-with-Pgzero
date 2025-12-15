from pgzero.actor import Actor
import random
import pygame
from maps import *

from enemy import *

###############################################################################
# Constants and Global Variables
###############################################################################

CELL_SIZE = 64 # Tamanho das células

TITLE = "WeCode e Dragões" # Título do jogo

FPS = 60

## Estados Globais ##

mode = "game"

###############################################################################
# CELLS AND MAP
###############################################################################

def __resize_actor_surface__(actor: Actor, size: int) -> None:
    """Change the Actor surface to <size> x <size>
    
    Args:
        actor: The Actor object.
        size: The side size in px.
    
    Side effects:
        Change the actor surface to size x size.
    """
    actor._surf = pygame.transform.scale(actor._surf, (size, size))

TILES = {"0": 'border',
         "1": 'floor',
         "2": 'floor_debris',
         }

map = map_2

MAP_SIZE_WIDTH = len(map[0])   # MAP: Map width

UI_BAR = ["-" for i in range(MAP_SIZE_WIDTH)]

MAP_SIZE_HEIGHT = len(map) + 1 # MAP: Map height

map.insert(0, UI_BAR)

WIDTH = CELL_SIZE * MAP_SIZE_WIDTH   # SCREEN: Screen Width
HEIGHT = CELL_SIZE * MAP_SIZE_HEIGHT # SCREEN: Screen Height

VALID_AREA_X = (1, MAP_SIZE_WIDTH - 2)
VALID_AREA_Y = (2, MAP_SIZE_HEIGHT - 2)

def get_cell_value(coordinate: tuple[int, int]):
    """"""
    x, y = coordinate

    return map[y][x]

def get_coordinate_in_map(coordinate: tuple[int, int]):
    """"""
    x, y = coordinate


    return (int(x / CELL_SIZE), int(y / CELL_SIZE))

def __convert_coordinate_to_px__(coordinate: tuple[int, int]) -> tuple[int, int]:
    x, y = coordinate

    return (x * CELL_SIZE, y * CELL_SIZE)

def draw_map_cell(cell: Actor, i: int, j: int):
    """"""
    __resize_actor_surface__(cell, CELL_SIZE)

    cell.left = CELL_SIZE * j
    cell.top = CELL_SIZE * i
    cell.draw()

def map_draw():
    for i in range(MAP_SIZE_HEIGHT):
        for j in range(MAP_SIZE_WIDTH):
            map_value = map[i][j]

            if map_value == "-":
                continue

            if map_value == "1": #TODO: Create randoness in floor blocks
                pass

            map_cell = Actor(TILES[map_value])

            draw_map_cell(map_cell, i, j)

###############################################################################
# PLAYER
###############################################################################

char = Actor('stand', topleft=(CELL_SIZE, CELL_SIZE * 2))

__resize_actor_surface__(char, CELL_SIZE)

char.health = 100
char.attack = 5

def __player_collide_with_wall__(new_coordinate: tuple[int, int]) -> bool:
    new_cell_value = get_cell_value(new_coordinate)

    if new_cell_value == "0":
        return True

    return False

def player_battle(enemy_index: int):
    enemy = enemies[enemy_index]

    enemy.health -= char.attack
    char.health -= enemy.attack

    if enemy.health <= 0:
        enemies.remove(enemy)

def player_movement():
    new_x = char.x
    new_y = char.y

    if keyboard.right:
        new_x += CELL_SIZE

    elif keyboard.left:
        new_x -= CELL_SIZE

    elif keyboard.down:
        new_y += CELL_SIZE

    elif keyboard.up:
        new_y -= CELL_SIZE

    new_coordinate = get_coordinate_in_map((new_x, new_y))

    if not __player_collide_with_wall__(new_coordinate):
        enemy_collide = __player_will_collide_with_enemy__(new_coordinate)
        if enemy_collide == -1:
            char.x = new_x
            char.y = new_y
        else:
            player_battle(enemy_collide)

###############################################################################
# ENEMIES 
############################################################################### 

def __get_valid_spawnpoint__(enemies_coordinates: list, max_tries: int):

    for i in range(max_tries):
        x = random.randint(VALID_AREA_X[0], VALID_AREA_X[1]) * CELL_SIZE
        y = random.randint(VALID_AREA_Y[0], VALID_AREA_Y[1]) * CELL_SIZE

        coordinate = get_coordinate_in_map((x, y))

        if get_cell_value(coordinate) != "0" and not (coordinate in enemies_coordinates):
            enemies_coordinates.append(coordinate)
            return coordinate

    return (-1, -1)

enemies = []
enemies_coordinates = []

for i in range(5):
    spawnpoint = __convert_coordinate_to_px__(__get_valid_spawnpoint__(enemies_coordinates, 20))

    if spawnpoint != (-1, -1):
        enemy = Ghost(topleft=spawnpoint, cell_size=CELL_SIZE)
        enemies.append(enemy)

def draw_enemies():
    """Function to draw the list of enemies"""
    for enemy in enemies:
        enemy.draw()
        screen.draw.text(str(enemy.health), center=(enemy.x + 30, enemy.y - 10), color='white', fontsize=30)

def __player_will_collide_with_enemy__(player_coordinate: tuple[int, int]):
    """"""
    for i, enemy in enumerate(enemies):
        if player_coordinate == enemy.coordinate:
            return i
    
    return -1

###############################################################################
# UI 
###############################################################################

life_border = Actor('life_border', topleft=(0, 0))
attack_border = Actor('attack_border', topleft=(128, 0))

def ui_draw():
    """Draw the User Interface"""
    life_border.draw()
    screen.draw.text(str(char.health), center=(life_border.x, life_border.y), color = '#b50d0d', fontname='belligoes',
                     fontsize=28)
    attack_border.draw()
    screen.draw.text(str(char.attack), center=(attack_border.x, attack_border.y), color = 'white', fontname='belligoes',
                     fontsize=30)
            
###############################################################################
# MAIN 
###############################################################################

# Draws
def draw():
    if mode == 'game':

        # MAP #
        screen.fill("#2f3542")
        map_draw()

        # PLAYER #
        char.draw()

        # HUD #
        ui_draw()

        # ENEMIES #
        draw_enemies()

# Keyboard
def on_key_down(key):

    player_movement()

# Lógica dos bônus
def update(dt):
    pass
