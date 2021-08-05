import math
from abc import ABC, abstractmethod

def in_range(enemy, tower):
    x1, y1 = enemy.rect.center
    x2, y2 = tower.rect.center
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if distance <= tower.get_range():
        return True
    return False

class AttackStrategy(ABC):
    """Abstract class of attack method"""
    @ abstractmethod
    def attack(self, enemies, tower, cd_count):
        raise NotImplementedError("Please implement this method")

class SingleAttack(AttackStrategy):
    """attack an enemy once a time"""
    def attack(self, enemies, tower, cd_count):
        for en in enemies.get():
            if in_range(en, tower):
                en.health -= tower.get_damage()
                cd_count = 0
                return cd_count#跑完第一隻就結束,代表只攻擊一次
        return cd_count

class AOE(AttackStrategy):
    """attack all the enemy in range once a time"""
    def attack(self, enemies, tower, cd_count):
        for en in enemies.get():
            if in_range(en, tower):
                en.health -= tower.get_damage()
                cd_count = 0
        #整個迴圈都跑完,代表整波敵人都會受到攻擊
        return cd_count

