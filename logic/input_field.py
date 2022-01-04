import pygame
from pygame.rect import Rect
from pygame_textinput import *
import logic.constants


class Input_Field:
    def __init__(self, font_size, font_color, cursor_width, cursor_blink_interval, cursos_color, rect, validator=None,
                 initial=''):
        self.font = pygame.font.Font(logic.constants.FONT_PATH, font_size)
        self.manager = TextInputManager(
            validator=lambda input: eval(validator),
            initial=str(initial))
        self.textinput = TextInputVisualizer(manager=self.manager, font_object=self.font)
        self.textinput.cursor_width = cursor_width
        self.textinput.cursor_blink_interval = cursor_blink_interval
        self.textinput.antialias = False
        self.textinput.font_color = font_color
        self.textinput.cursor_color = cursos_color
        self.rect = self.textinput.surface.get_rect(center=rect)
        self.border_rect = Rect(self.rect.x - 10 * logic.constants.SCREEN_CONST,
                                self.rect.y - 10 * logic.constants.SCREEN_CONST,
                                self.rect.width - 10 * logic.constants.SCREEN_CONST,
                                self.rect.height + 15 * logic.constants.SCREEN_CONST)
