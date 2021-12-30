import pygame
import pygame.rect
import logic.constants


class Text:
    def __init__(self, text, size, pos, color):
        self.text = text
        self.color = color
        self.font = pygame.font.Font(logic.constants.FONT_PATH, size)
        self.text = self.font.render(self.text, True, self.color)
        self.rect = pygame.Rect(*pos, *self.text.get_size())
        self.rect = self.text.get_rect(center=(self.rect.x, self.rect.y))
