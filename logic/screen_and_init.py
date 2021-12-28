from logic.imports import *


def init(size):
    pygame.init()
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Lego Master')
    return screen, clock
