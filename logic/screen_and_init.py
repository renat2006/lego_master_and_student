import pygame

from logic.imports import *
import logic.constants


def init(size):
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    logic.constants.SIZE = logic.constants.WIDTH, logic.constants.HEIGHT = screen.get_size()

    clock = pygame.time.Clock()
    pygame.display.set_caption('Lego Master')
    return screen, clock
