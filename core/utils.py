import pygame

def resize_actor(actor, size):
    actor._surf = pygame.transform.scale(actor._surf, (size, size))

def tint_actor_red(actor):
    tinted = actor._surf.copy()
    tinted.fill((255, 0, 0, 255), special_flags=pygame.BLEND_RGBA_MULT)
    actor._surf = tinted

def reset_actor_tint(actor):
    actor._surf = actor._base_surf.copy()



