from pgzero.actor import Actor
from core.constants import CELL_SIZE
from core.utils import resize_actor

class Player(Actor):
    def __init__(self):
        super().__init__('stand', topleft=(CELL_SIZE, CELL_SIZE * 2))
        resize_actor(self, CELL_SIZE)

        self.health = 100
        self.attack = 5

