from abc import ABC, abstractmethod
import pygame
import os
from tower.attack_strategy import AOE, SingleAttack ,Slowly
from settings import WIN_WIDTH, WIN_HEIGHT

#攻擊的塔
MASK_IMAGE= pygame.transform.scale(pygame.image.load(os.path.join("images", "mask.png")), (70, 70))
ALCOHOL_IMAGE= pygame.transform.scale(pygame.image.load(os.path.join("images", "alcohol.png")), (60, 70))
INJECTION_IMAGE= pygame.transform.scale(pygame.image.load(os.path.join("images", "injection.png")), (60, 70))
FOREHEAD_GUN_IMAGE= pygame.transform.scale(pygame.image.load(os.path.join("images", "forehead_gun.png")), (60, 60))
#黃色點點
PLOT_IMAGE= pygame.transform.scale(pygame.image.load(os.path.join("images", "vacant_lot.png")), (20, 20))

class Vacancy:
    def __init__(self,x,y):
        self.image=PLOT_IMAGE;
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)

    def clicked(self, x: int, y: int) -> bool:
        return True if self.rect.collidepoint(x, y) else False
    '''def draw(self, win):
        win.blit(self.image, self.rect)'''

class Tower:
    def __init__(self, x: int, y: int, attack_strategy, image):
        self.image = image  # image of the tower
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # center of the tower
        self.level = 0  # level of the tower
        self._range = [100, 110, 120, 130, 140, 150]  # tower attack range
        self._damage = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5]  # tower damage
        self.cd_count = 0  # used in self.is_cool_down()
        self.cd_max_count = 60  # used in self.is_cool_down()
        self.attack_strategy = attack_strategy  # chose an attack strategy (AOE, single attack ....)
        self.value = [200, 250, 300, 350, 450]

    @classmethod
    def Mask(cls, x, y):  # 口罩,攻擊方式目前暫訂單體攻擊
        mask = cls(x, y, SingleAttack(), MASK_IMAGE)
        mask._range = [130, 140, 150, 160, 170, 180]
        mask._damage = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5]
        mask.value=[200,250,300,350,450,500]
        return mask

    @classmethod
    def Alcohol(cls, x, y):  # 酒精,全體攻擊
        alcohol = cls(x, y, AOE(), ALCOHOL_IMAGE)
        alcohol._range = [130, 140, 150, 160, 170, 180]
        alcohol._damage = [1.5, 1.7, 1.9, 2.1, 2.3,2.5]
        alcohol.value = [250, 270, 310, 350, 410,450]
        return alcohol

    @classmethod
    def Injection(cls, x, y):  # 打針,單體攻擊
        injection = cls(x, y, SingleAttack(), INJECTION_IMAGE)
        injection._range = [130, 140, 150, 160, 170, 180]
        injection._damage = [3.0, 3.1, 3.2, 3.3, 3.4, 3.5]
        injection.value = [200, 220, 250, 280, 330,380]
        return injection

    @classmethod
    def Foreheadgun(cls, x, y):  # 額溫槍,全體攻擊+緩速
        foreheadgun = cls(x, y, SingleAttack(), FOREHEAD_GUN_IMAGE)
        foreheadgun._range = [130, 140, 150, 160, 170, 180]
        foreheadgun._damage = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
        foreheadgun.value = [300, 330, 390 ,450 , 500,560]
        return foreheadgun

    def attack(self, enemy_group):
        # cd
        if self.cd_count < self.cd_max_count:
            self.cd_count += 1
            return
        # syntax: attack_strategy().attack(tower, enemy_group, cd_count)
        # It's something like you hire a "Strategist" to decide how to attack the enemy
        # according to the the input parameters.
        # You can add other ways of attack just by expanding the "attack_strategy.py"
        self.cd_count = self.attack_strategy.attack(enemy_group, self, self.cd_count)

    '''以下兩個函式可以將升級後or賣出後,加錢or減錢'''
    def get_upgrade_cost(self):
        return self.value[self.level+1] - self.value[self.level]

    def get_cost(self):
        return self.value[self.level]

    @property
    def range(self):
        return self._range[self.level]

    @property
    def damage(self):
        return self._damage[self.level]

    def clicked(self, x, y):
        return True if self.rect.collidepoint(x, y) else False

    '''def draw_effect_range(self, win):
        """
        draw the tower effect range, which is a transparent circle.
        印出半透明的圓
        """
        surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        transparency = 120
        pygame.draw.circle(surface, (128, 128, 128, transparency), self.rect.center, self._range[self.level])
        win.blit(surface, (0, 0))'''