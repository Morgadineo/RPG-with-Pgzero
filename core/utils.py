import pygame

def resize_actor(actor, size):
    actor._surf = pygame.transform.scale(actor._surf, (size, size))

def map_to_cell(pos: tuple[int, int], cell_size: int):
    return int(pos[0] / cell_size), int(pos[1] / cell_size)

def cell_to_px(cell, cell_size):
    return cell[0] * cell_size, cell[1] * cell_size

