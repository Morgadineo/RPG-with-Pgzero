def try_move(entity, dx, dy, world):
    new_x = entity.x + dx
    new_y = entity.y + dy

    cell = int(new_x / 64), int(new_y / 64)

    if not world.is_wall(cell):
        entity.x = new_x
        entity.y = new_y

