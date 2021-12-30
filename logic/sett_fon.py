import pygame
import logic.constants
from pygame.rect import *

class Settings_fon:
    def __init__(self, screen, pos, size, color):
        self.screen = screen
        self.pos = pos
        self.size = size
        self.color = color
        self.rect = Rect(*pos, *size)
    def draw(self):
        self.set_fon = pygame.draw.rect(self.screen, self.color,
                                        self.rect)
        pygame.draw.rect(self.screen, 'red', self.rect, 10)
