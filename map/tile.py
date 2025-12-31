from pgzero.actor import Actor

class Tile(Actor):
    
    def __init__(self, id, image: str, walkable: bool):
        self.id = id
        self.walkable = walkable

        super().__init__('dummy')

        self._surf = image

        self._update_pos()

class Wall(Tile):
    
    def __init__(self, id, image: str):

        super().__init__(id, image, walkable=False)

class Floor(Tile):
    
    def __init__(self, id, image: str):

        super().__init__(id, image, walkable=True)

class Door(Floor):
    def __init__(self, id, image: str):

        super().__init__(id, image)

class SpawnDoor(Door):

    def __init__(self, id, image: str):
        super().__init__(id, image)
