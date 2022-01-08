import random

import pygame
import logic.constants
from logic.particle import Particle

loot_group = pygame.sprite.Group()


class Loot(pygame.sprite.Sprite):
    def __init__(self, image, bonus, pos_x, pos_y):
        super().__init__(loot_group)

        self.image = image
        self.norm_im = image
        self.mask = pygame.mask.from_surface(self.image)
        self.add(loot_group)
        self.rect = self.image.get_rect().move(
            logic.constants.tile_width * pos_x, logic.constants.tile_height * pos_y)
        self.bonus_effect = bonus
        self.counter = 0
        self.move_top = 10


