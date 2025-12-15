from pgzero.actor import Actor
import pygame
from random import randint

class Enemy(Actor):
    def __init__(self, 
                 sprite: str, 
                 topleft: tuple[int, int],
                 life: int,
                 attack: int,
                 cell_size: int):

        super().__init__(sprite, topleft=topleft)

        self._surf = pygame.transform.scale(self._surf, (cell_size, cell_size))

        self.health = life
        self.attack = attack
        self.coordinate = (int(self.x / cell_size), int(self.y / cell_size))

    def movement(self):
        self.movement


class Ghost(Enemy):
    def __init__(self, topleft: tuple[int, int], cell_size: int):
        super().__init__(
            sprite='enemies/ghost',
            topleft=topleft,
            life=10,
            attack=5,
            cell_size=cell_size
        )

