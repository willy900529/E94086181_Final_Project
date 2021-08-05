import pygame
import os
from enemy import EnemyGroup
from tower_group import TowerGroup
from settings import WIN_WIDTH, WIN_HEIGHT

# load image
BACKGROUND_IMAGE = pygame.image.load(os.path.join("images", "NCKU_MAP.png"))
'''HP_IMAGE = pygame.image.load(os.path.join("images", "hp.png"))
HP_GRAY_IMAGE = pygame.image.load(os.path.join("images", "hp_gray.png"))'''


class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.bg_image = pygame.transform.scale(BACKGROUND_IMAGE, (WIN_WIDTH, WIN_HEIGHT))
        '''self.hp_images = [pygame.transform.scale(HP_IMAGE, (40, 40)),
                          pygame.transform.scale(HP_GRAY_IMAGE, (40, 40))]'''
        self.hp = 10
        self.max_hp = 10
        self.money = 100
        self.enemies = EnemyGroup()
        self.towers = TowerGroup()

    def draw(self):
        """
        Draw everything in this method.
        :return: None
        """
        # draw background
        self.win.fill((255, 255, 255))
        self.win.blit(self.bg_image, (0, 0))
        # draw enemies
        self.enemies.draw(self.win)
        # draw towers
        self.towers.draw(self.win)
        pygame.display.update()

    def update(self):
        game_quit = False
        # event loop
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
                return game_quit
            # player press action
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n and self.enemies.is_empty():
                    self.enemies.add(10)  # generate  10 enemy for the next wave
            # player click action
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.towers.got_click(mouse_x, mouse_y)

        # update tower action
        self.towers.update(self.enemies)
        # update enemy action
        self.enemies.update()
        return game_quit

