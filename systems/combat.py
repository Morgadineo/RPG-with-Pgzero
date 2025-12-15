def battle(attacker, defender):
    defender.health -= attacker.attack
    attacker.health -= defender.attack

