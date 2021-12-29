import pygame

from logic.load_image import *

# Код Димы--------------------------------------
player_group = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, player_image, pos):
        super().__init__(player_group)
        self.image = load_image(player_image, -1)
        self.clock = pygame.time.Clock()
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.player_width = self.image.get_rect().width
        self.player_height = self.image.get_rect().height
        self.rect = self.image.get_rect().move(
            self.pos_x, self.pos_y)

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
