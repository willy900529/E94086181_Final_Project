import pygame
from game import Game
from settings import FPS

if __name__ == '__main__':
    # initialization
    pygame.init()
    # set the window
    pygame.display.set_caption("My TD game")

    covid_game = Game()
    quit_game = False
    while not quit_game:
        pygame.time.Clock().tick(FPS)
        quit_game = covid_game.update()
        covid_game.draw()

    pygame.quit()
