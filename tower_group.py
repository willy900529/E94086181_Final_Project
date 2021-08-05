import pygame
from tower_factory import Vacancy, Tower
from menus import UpgradeMenu, BuildMenu

pygame.init()

class TowerGroup:
    def __init__(self):
        self.__towers = [] #一開始的遊戲畫面
        self.__plots = [Vacancy(110, 448), Vacancy(331, 444),Vacancy(179, 160),Vacancy(291, 157),
                        Vacancy(417, 163),Vacancy(338, 296),Vacancy(233, 295),Vacancy(142, 292),
                        Vacancy(496, 294),Vacancy(584, 167),Vacancy(498, 444),Vacancy(582, 297)] #一開始的遊戲增加點位
        self.selected_tower = None
        self.selected_plot = None
        self.selected_menu = None
        self.button_response = None

    def update(self, enemy_group):
        """
        Update the tower action. (This function is call in main game loop)
        """
        for tw in self.__towers:
            tw.attack(enemy_group)
        # upgrade, sell, and add tower
        if self.button_response == "upgrade":
            self.upgrade()
        elif self.button_response == "sell":
            self.sell()
        else:
            tower_name = self.button_response
            self.add_tower(tower_name)

        # call menu
        self.call_menu()
        self.button_response = None

    def draw(self, win) -> None:
        # draw vacancy 畫黃色點點
        for pt in self.__plots:
            pt.draw(win)
        # draw tower
        for tw in self.__towers:
            win.blit(tw.image, tw.rect)
        # draw tower range and upgrade menu
        if self.selected_tower is not None:
            self.selected_tower.draw_effect_range(win)  # 將點擊之塔的半透明圓給畫出來
            self.selected_menu.draw(win)
        # draw vacant lot and build menu
        elif self.selected_plot is not None:  # 如果塔的位置是空的,將黃色點點畫出來
            self.selected_menu.draw(win)

    def got_click(self, x: int, y: int):
        """
        The tower group response to the player click action. (1) select the tower OR (2) get button response
        (This method is call in main game loop)
        :param x: mouse x
        :param y: mouse y
        :return: None
        """
        # if the item is clicked, select the item
        for tw in self.__towers:
            if tw.clicked(x, y):
                self.selected_tower = tw
                self.selected_plot = None
                break
        for pt in self.__plots:
            if pt.clicked(x, y):
                self.selected_tower = None
                self.selected_plot = pt
                break
        # if the button is clicked, get the button response.
        # and keep selecting the tower/plot.
        if self.selected_menu is not None:
            for btn in self.selected_menu.get_buttons():
                if btn.clicked(x, y):
                    self.button_response = btn.response()
            if self.button_response is None:
                self.selected_tower = None
                self.selected_plot = None

    def call_menu(self):
        """
        call upgrade menu/ build menu
        :return:
        """
        if self.selected_tower is not None:
            x, y = self.selected_tower.rect.center
            new_menu = UpgradeMenu(x, y)
            self.selected_menu = new_menu
        elif self.selected_plot is not None:
            x, y = self.selected_plot.rect.center
            new_menu = BuildMenu(x, y)
            self.selected_menu = new_menu
        else:
            self.selected_menu = None

    def upgrade(self):  # 升級
        """
        Upgrade the selected tower (tower level + 1).
        :return: None
        """
        if self.selected_tower.level < 5:
            self.selected_tower.level += 1

    def sell(self):  # 賣出
        """
        Sell the tower (remove from self.__towers)
        :return: None
        """
        x, y = self.selected_tower.rect.center
        self.__plots.append(Vacancy(x, y))
        self.__towers.remove(self.selected_tower)
        self.selected_tower = None

    def add_tower(self, tower_name: str):
        """
        (Q2) Add new tower to the tower list (self.__tower)
        :param tower_name: str
        :return: None
        """
        if tower_name is None:
            return
        x, y = self.selected_plot.rect.center
        if tower_name == "mask(":
            new_tower = Tower.Mask(x, y)
        elif tower_name == "alcohol":
            new_tower = Tower.Alcohol(x, y)
        elif tower_name == "injection":
            new_tower = Tower.Injection(x, y)
        else:
            return
        self.__towers.append(new_tower)
        self.__plots.remove(self.selected_plot)
        self.selected_plot = None

    def get(self):  # 回傳整個塔(全部的塔)
        return self.__towers