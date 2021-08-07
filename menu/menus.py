import pygame
import os

pygame.init()

#menu,升級,賣出圖片
MENU_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "upgrade_menu.png")), (200, 200))
UPGRADE_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "upgrade.png")), (60, 35))
SELL_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "sell.png")), (40, 40))

#四個塔的圖片
INJECTION_BTN_IMAGE  = pygame.transform.scale(pygame.image.load(os.path.join("images", "injection.png")), (40, 40))
MASK_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "mask.png")), (56, 56))
ALCOHOL_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "alcohol.png")), (40, 40))
FOREHEAD_GUN_IMAGE= pygame.transform.scale(pygame.image.load(os.path.join("images", "forehead_gun.png")), (40, 40))

class Button:
    def __init__(self, image, name: str, x: int, y: int):
        self.image = image
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x, y):
        return True if self.rect.collidepoint(x, y) else False

    @property
    def response(self):
        return self.name

class Menu:
    def __init__(self, x: int, y: int):
        self.image = MENU_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self._buttons = []

    '''def draw(self, win):
        win.blit(self.image, self.rect)
        for btn in self._buttons:
            win.blit(btn.image, btn.rect)'''

    @property
    def get_buttons(self):
        return self._buttons

class UpgradeMenu(Menu):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._buttons = [Button(UPGRADE_BTN_IMAGE, "upgrade", self.rect.centerx, self.rect.centery - 70),
                         Button(SELL_BTN_IMAGE, "sell", self.rect.centerx, self.rect.centery + 75),
                         ]

class BuildMenu(Menu):
    def __init__(self, x, y):
        super().__init__(x, y)
        """
        button name: mask , injection , alcohol
        """
        self._buttons.extend([Button(MASK_IMAGE, "mask", self.rect.centerx, self.rect.centery+78),
                             Button(INJECTION_BTN_IMAGE, "injection", self.rect.centerx-69, self.rect.centery+9),
                              Button(ALCOHOL_BTN_IMAGE, "alcohol", self.rect.centerx, self.rect.centery-70),
                             Button(FOREHEAD_GUN_IMAGE, "foreheadgun", self.rect.centerx+69, self.rect.centery+9)])













