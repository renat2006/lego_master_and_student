import pygame
import logic.constants
from logic.load_image import load_image
from logic.term import terminate
from logic.text import *


def final_screen(screen, clock, points):
    pygame.mixer.music.load('data/music/last.mp3')
    pygame.mixer.music.play(-1)
    fon = pygame.transform.scale(load_image(logic.constants.MENU_FON_PATH), (logic.constants.SIZE))
    screen.blit(fon, (0, 0))

    f_text = Text(str(int(points[0])), 200, (100, 100), 'black').text
    con_text = Text('Вы набрали:', 75, (100, 100), 'black').text
    screen.blit(con_text, (
        logic.constants.WIDTH // 2 - con_text.get_width() // 2,
        logic.constants.HEIGHT // 2 + con_text.get_height() // 2 - 30 - con_text.get_height()))
    screen.blit(f_text, (
        logic.constants.WIDTH // 2 - f_text.get_width() // 2, logic.constants.HEIGHT // 2 + f_text.get_height() // 4))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(logic.constants.FPS)
