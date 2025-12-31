from pgzero.actor import Actor

life_border = Actor('ui/life_border', topleft=(0, 0))
attack_border = Actor('ui/attack_border', topleft=(128, 0))

def draw(player, screen):
    life_border.draw()
    screen.draw.text(str(player.health), center=life_border.pos)

    attack_border.draw()
    screen.draw.text(str(player.attack), center=attack_border.pos)

