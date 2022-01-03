import pygame

from logic.imports import *
import logic.constants


# Код Рената --------------------------------------
def init(size):
    pygame.init()
    if size == (0, 0):
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(size)

    logic.constants.SIZE = logic.constants.WIDTH, logic.constants.HEIGHT = screen.get_size()
    logic.constants.SCREEN_CONST = (logic.constants.WIDTH * logic.constants.HEIGHT) / (1920 * 1080)

    logic.constants.HEADING_FONT_SIZE = int(75 * logic.constants.SCREEN_CONST)
    logic.constants.MAIN_TEXT_SIZE = int(60 * logic.constants.SCREEN_CONST)


    clock = pygame.time.Clock()
    pygame.display.set_caption('Lego Master')
    return screen, clock
