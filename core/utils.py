import pygame

def resize_actor(actor, size):
    actor._surf = pygame.transform.scale(actor._surf, (size, size))

