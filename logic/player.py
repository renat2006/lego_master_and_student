import pygame

from logic.load_image import *
import logic.constants

# Код Димы--------------------------------------
player_group = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(player_group)
        player_image = load_image(logic.constants.PLAYER_IMAGE_PATH)
        self.image = player_image
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.clock = pygame.time.Clock()
        self.pos_x = x * logic.constants.player_width
        self.pos_y = y * logic.constants.player_height
        self.player_width = self.image.get_rect().width
        self.player_height = self.image.get_rect().height
        self.rect = self.image.get_rect().move(
            self.pos_x, self.pos_y)
        self.jumping = False
    def link_to_surface(self, surface):
        self.screen = surface

    def move(self, x, y):
        self.rect = self.rect.move(x, y)

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
        #pygame.time.delay(15)
