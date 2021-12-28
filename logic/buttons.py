from logic.imports import *
from logic.constants import *


class Buttons:
    def __init__(self, b_text, color, pos, screen):
        self.text = b_text
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        font = pygame.font.Font(None, 50)
        self.text = font.render(b_text, True, color)

        screen.blit(self.text, (self.pos_x, self.pos_y))
