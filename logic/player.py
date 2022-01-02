import pygame

from logic.load_image import *
from logic.constants import PLAYER_IMAGE_PATH, JUMP_VALUE, STEP

# Код Димы--------------------------------------
player_group = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(player_group)
        self.image = load_image(PLAYER_IMAGE_PATH, -1)
        self.clock = pygame.time.Clock()

        self.pos_x = x
        self.pos_y = y
        self.player_width = self.image.get_rect().width
        self.player_height = self.image.get_rect().height
        self.rect = self.image.get_rect().move(
            self.pos_x, self.pos_y)

        self.jumping = False

    def link_to_surface(self, surface):
        self.screen = surface

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def set_jump(self):
        if self.is_jump():
            self.jumping = False
        else:
            self.jumping = True

    def is_jump(self, jump=False):
        if self.jumping:
            return True
        return False

    def next_jump_stage(self, jump_stage):
        self.move(0, jump_stage)
        pygame.time.delay(15)
