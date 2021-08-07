import pygame
import os

# image
BACKGROUND_IMAGE = pygame.image.load(os.path.join("images", "NCKU_MAP.png"))

# screen size
WIN_WIDTH = 1024
WIN_HEIGHT = 576
# frame rate
FPS = 60
# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (147, 0, 147)

# enemy path
# 打開txt檔
fileObject = open("paths/path_1.txt ", 'r')
# 讀取一行內容
line = fileObject.readline()
# 將內容append進[]
PATH_1 = []
while line:
    PATH_1.append(eval(line))
    line = fileObject.readline()
# 關閉txt檔
fileObject.close()

# 打開txt檔
fileObject = open("paths/path_2.txt ", 'r')
# 讀取一行內容
line = fileObject.readline()
# 將內容append進[]
PATH_2 = []
while line:
    PATH_2.append(eval(line))
    line = fileObject.readline()
# 關閉txt檔
fileObject.close()

# 打開txt檔
fileObject = open("paths/path_3.txt ", 'r')
# 讀取一行內容
line = fileObject.readline()
# 將內容append進[]
PATH_3 = []
while line:
    PATH_3.append(eval(line))
    line = fileObject.readline()
# 關閉txt檔
fileObject.close()

# 打開txt檔
fileObject = open("paths/vacancy.txt ", 'r')
# 讀取一行內容
line = fileObject.readline()
# 將內容append進[]
VACANCY = []
while line:
    VACANCY.append(eval(line))
    line = fileObject.readline()
# 關閉txt檔
fileObject.close()
# base
BASE = pygame.Rect(415, 535, 50, 50)
