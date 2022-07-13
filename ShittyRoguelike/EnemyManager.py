from Enemies import Enemy
import random

class EnemyManager(Enemy):
    def __init__(self):
        pass   

    def spawn_enemy(self):
        goblin = Enemy("Goblin",150 * random.randint(1,4),random.randint(2,3),False)
        orc = Enemy("Orc",150 * random.randint(2,5),random.randint(3,5),False)
        enemies = []
        enemies.append(goblin)
        enemies.append(orc)
        return enemies

