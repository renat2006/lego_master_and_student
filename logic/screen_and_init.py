import pygame

from logic.imports import *
import logic.constants


# Код Рената --------------------------------------
def init(size, vol=0.7):
    pygame.mixer.pre_init(44100, -16, 1, 512)

    pygame.init()
    pygame.mixer.music.load(logic.constants.MUSIC_PATH)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(vol)
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
