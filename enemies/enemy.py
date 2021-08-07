import pygame
import math
import os
from settings import PATH_1, PATH_2, PATH_3, BASE
from color_settings import *



pygame.init()
GREEN_ENEMY_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "GreenEnemy.png")), (50, 50))
RED_ENEMY_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "RedEnemy.png")), (50, 50))
PURPLE_ENEMY_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "PurpleEnemy.png")), (50, 50))
BLACK_ENEMY_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "BlackEnemy.png")), (50, 50))

class GreenEnemy:
    def __init__(self):
        self.max_health = 5
        self.health = self.max_health
        self.path = PATH_2
        self.path_index = 0
        self.move_count = 0
        self.stride = 1
        self.image = GREEN_ENEMY_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]
        self.__expedition = []


    def move(self):
        x1, y1 = self.path[self.path_index]
        x2, y2 = self.path[self.path_index + 1]
        distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        max_count = int(distance / self.stride)

        # compute the unit vector
        unit_vector_x = (x2 - x1) / distance
        unit_vector_y = (y2 - y1) / distance

        # compute the movement
        delta_x = unit_vector_x * self.stride * self.move_count
        delta_y = unit_vector_y * self.stride * self.move_count

        # update the position and counter
        if self.move_count <= max_count:
            self.rect.center = (x1 + delta_x, y1 + delta_y)
            self.move_count += 1
        else:
            self.move_count = 0
            self.path_index += 1
            self.rect.center = self.path[self.path_index]


    def draw(self, win):
        for en in self.__expedition:
            win.blit(en.image, en.rect)

            # draw health bar
            bar_width = en.rect.w * (en.health / en.max_health)
            max_bar_width = en.rect.w
            bar_height = 5
            pygame.draw.rect(win, RED, [en.rect.x, en.rect.y - 10, max_bar_width, bar_height])
            pygame.draw.rect(win, GREEN, [en.rect.x, en.rect.y - 10, bar_width, bar_height])
    def stride_revise(self):
        self.stride=0.8


class RedEnemy:
    def __init__(self):
        self.max_health = 8
        self.health = self.max_health
        self.path = PATH_1
        self.path_index = 0
        self.move_count = 0
        self.stride = 1
        self.image = RED_ENEMY_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]
        self.__expedition = []


    def move(self):
        x1, y1 = self.path[self.path_index]
        x2, y2 = self.path[self.path_index + 1]
        distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        max_count = int(distance / self.stride)

        # compute the unit vector
        unit_vector_x = (x2 - x1) / distance
        unit_vector_y = (y2 - y1) / distance

        # compute the movement
        delta_x = unit_vector_x * self.stride * self.move_count
        delta_y = unit_vector_y * self.stride * self.move_count

        # update the position and counter
        if self.move_count <= max_count:
            self.rect.center = (x1 + delta_x, y1 + delta_y)
            self.move_count += 1
        else:
            self.move_count = 0
            self.path_index += 1
            self.rect.center = self.path[self.path_index]


    def draw(self, win):
        for en in self.__expedition:
            win.blit(en.image, en.rect)

            # draw health bar
            bar_width = en.rect.w * (en.health / en.max_health)
            max_bar_width = en.rect.w
            bar_height = 5
            pygame.draw.rect(win, RED, [en.rect.x, en.rect.y - 10, max_bar_width, bar_height])
            pygame.draw.rect(win, GREEN, [en.rect.x, en.rect.y - 10, bar_width, bar_height])

class PurpleEnemy:
    def __init__(self):
        self.max_health = 10
        self.health = self.max_health
        self.path = PATH_3
        self.path_index = 0
        self.move_count = 0
        self.stride = 1
        self.image = PURPLE_ENEMY_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]
        self.__expedition = []


    def move(self):
        x1, y1 = self.path[self.path_index]
        x2, y2 = self.path[self.path_index + 1]
        distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        max_count = int(distance / self.stride)

        # compute the unit vector
        unit_vector_x = (x2 - x1) / distance
        unit_vector_y = (y2 - y1) / distance

        # compute the movement
        delta_x = unit_vector_x * self.stride * self.move_count
        delta_y = unit_vector_y * self.stride * self.move_count

        # update the position and counter
        if self.move_count <= max_count:
            self.rect.center = (x1 + delta_x, y1 + delta_y)
            self.move_count += 1
        else:
            self.move_count = 0
            self.path_index += 1
            self.rect.center = self.path[self.path_index]


    def draw(self, win):
        for en in self.__expedition:
            win.blit(en.image, en.rect)

            # draw health bar
            bar_width = en.rect.w * (en.health / en.max_health)
            max_bar_width = en.rect.w
            bar_height = 5
            pygame.draw.rect(win, RED, [en.rect.x, en.rect.y - 10, max_bar_width, bar_height])
            pygame.draw.rect(win, GREEN, [en.rect.x, en.rect.y - 10, bar_width, bar_height])

class BlackEnemy:
    def __init__(self):
        self.max_health = 15
        self.health = self.max_health
        self.path = PATH_3
        self.path_index = 0
        self.move_count = 0
        self.stride = 1
        self.image = BLACK_ENEMY_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]
        self.__expedition = []


    def move(self):
        x1, y1 = self.path[self.path_index]
        x2, y2 = self.path[self.path_index + 1]
        distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        max_count = int(distance / self.stride)

        # compute the unit vector
        unit_vector_x = (x2 - x1) / distance
        unit_vector_y = (y2 - y1) / distance

        # compute the movement
        delta_x = unit_vector_x * self.stride * self.move_count
        delta_y = unit_vector_y * self.stride * self.move_count

        # update the position and counter
        if self.move_count <= max_count:
            self.rect.center = (x1 + delta_x, y1 + delta_y)
            self.move_count += 1
        else:
            self.move_count = 0
            self.path_index += 1
            self.rect.center = self.path[self.path_index]


    def draw(self, win):
        for en in self.__expedition:
            win.blit(en.image, en.rect)

            # draw health bar
            bar_width = en.rect.w * (en.health / en.max_health)
            max_bar_width = en.rect.w
            bar_height = 5
            pygame.draw.rect(win, RED, [en.rect.x, en.rect.y - 10, max_bar_width, bar_height])
            pygame.draw.rect(win, GREEN, [en.rect.x, en.rect.y - 10, bar_width, bar_height])

class EnemyGroup:
    def __init__(self):
        self.campaign_count = 0
        self.campaign_max_count = 60
        self.__reserved_member = []
        self.__expedition = []
        self.wave = 0


    def update(self):
        self.campaign()
        for en in self.__expedition:
            en.move()
            if en.health <= 0:
                self.retreat(en)

            # delete the object when it reach the base
            if BASE.collidepoint(en.rect.centerx, en.rect.centery):
                self.retreat(en)

    def draw(self, win):
        for en in self.__expedition:
            win.blit(en.image, en.rect)
            # draw health bar
            bar_width = en.rect.w * (en.health / en.max_health)
            max_bar_width = en.rect.w
            bar_height = 5
            pygame.draw.rect(win, RED, [en.rect.x, en.rect.y - 10, max_bar_width, bar_height])
            pygame.draw.rect(win, GREEN, [en.rect.x, en.rect.y - 10, bar_width, bar_height])

    def campaign(self):
        """
        Enemy go on an expedition
        """
        if self.campaign_count > self.campaign_max_count and self.__reserved_member:
            self.__expedition.append(self.__reserved_member.pop())
            self.campaign_count = 0
        else:
            self.campaign_count += 1

    def add(self, num):
        """
        Generate the enemies for next wave
        """
        # 生成順序為 綠->紫->紅->黑
        if self.wave % 4 == 0:
            self.__reserved_member = [GreenEnemy() for _ in range(num)]
        elif self.wave % 4 == 1:
            self.__reserved_member = [PurpleEnemy() for _ in range(num)]
        elif self.wave % 4 == 2:
            self.__reserved_member = [RedEnemy() for _ in range(num)]
        else:
            self.__reserved_member = [BlackEnemy() for _ in range(num)]
        self.wave += 1

    def get(self):
        """
        Get the enemy list
        """
        return self.__expedition

    def is_empty(self):
        """
        Return whether the enemy is empty (so that we can move on to next wave)
        """
        return False if self.__reserved_member or self.__expedition else True

    def retreat(self, enemy):
        """
        Remove the enemy from the expedition
        :param enemy: class Enemy()
        :return: None
        """
        self.__expedition.remove(enemy)