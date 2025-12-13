from os import wait
from pgzero.actor import Actor
import random
import pygame

###############################################################################
# Constants and Global Variables
###############################################################################

MAP_SIZE_WIDTH = 10  # Largura do mapa
MAP_SIZE_HEIGHT = 11 # Altura do mapa

CELL_SIZE = 64 # Tamanho das células

WIDTH = CELL_SIZE * MAP_SIZE_WIDTH   # TELA: Largura da Tela
HEIGHT = CELL_SIZE * MAP_SIZE_HEIGHT # TELA: Altura da Tela

TITLE = "WeCode e Dragões" # Título do jogo

FPS = 60

## Estados Globais ##

win = 0
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

TILES = {0: 'border',
         1: 'floor',
         2: 'floor_debris',
         3: 'floor_rocks'}

VALID_AREA_X = (1, MAP_SIZE_WIDTH - 2)
VALID_AREA_Y = (2, MAP_SIZE_HEIGHT - 2)

map = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], # Linha usada para indicar os valores de vida e ataque
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
          [0, 1, 1, 2, 1, 3, 1, 1, 1, 0], 
          [0, 1, 1, 1, 2, 1, 1, 1, 1, 0], 
          [0, 1, 3, 2, 1, 1, 3, 1, 1, 0], 
          [0, 1, 1, 1, 1, 3, 1, 1, 1, 0], 
          [0, 1, 1, 3, 1, 1, 2, 1, 1, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def get_cell_value(coordinate: tuple[int, int]):
    """"""
    x, y = coordinate

    return map[y][x]

def get_coordinate_in_map(coordinate: tuple[int, int]):
    """"""
    x, y = coordinate


    return (int(x / CELL_SIZE), int(y / CELL_SIZE))

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

            if map_value < 0:
                continue

            map_cell = Actor(TILES[map_value])

            draw_map_cell(map_cell, i, j)

###############################################################################
# PLAYER
###############################################################################

char = Actor('stand')

__resize_actor_surface__(char, CELL_SIZE)

char.pos = (CELL_SIZE, CELL_SIZE * 2)
char.health = 100
char.attack = 5

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
    new_cell_value = get_cell_value(new_coordinate)

    print(new_coordinate)
    print(new_cell_value)

    if new_cell_value != 0:
        char.x = new_x
        char.y = new_y


###############################################################################
# ENEMIES 
###############################################################################

ENEMIES_DICT = {"Ghost": {'life': 10,
                          'attack': 5,
                          'sprite': 'enemies/ghost'},
                }

ghost = ENEMIES_DICT['Ghost']

enemies = []

for i in range(5):
    x = random.choice(VALID_AREA_X) * CELL_SIZE
    y = random.choice(VALID_AREA_Y) * CELL_SIZE
    enemy = Actor(ghost['sprite'], topleft = (x, y))

    __resize_actor_surface__(enemy, CELL_SIZE)

    enemy.health = ghost['life']
    enemy.attack = ghost['attack']
    enemies.append(enemy)


def draw_enemies():
    """Function to draw the list of enemies"""
    for enemy in enemies:
        enemy.draw()
        screen.draw.text(str(enemy.health), topleft=(enemy.x + 5, enemy.y - 30), color='white', fontsize=18)


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
    old_x = char.x
    old_y = char.y

    player_movement()
        
    # Colisão com inimigos
    enemy_index = char.collidelist(enemies)
    if enemy_index != -1:
        char.x = old_x
        char.y = old_y
        enemy = enemies[enemy_index]
        enemy.health -= char.attack
        char.health -= enemy.attack
        if enemy.health <= 0:
            # Adicionando os bônus
            enemies.pop(enemy_index)

# Lógica dos bônus
def update(dt):
    pass
