import pygame

from logic.imports import *
from logic.constants import *


class Buttons:
    def __init__(self, b_text, color, pos):
        self.text = b_text
        self.font = pygame.font.Font(FONT_PATH, 50)
        self.text = self.font.render(b_text, True, color)
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.rect = self.text.get_rect(center=(self.pos_x, self.pos_y))
        self.pos_x = self.rect.x
        self.pos_y = self.rect.y

