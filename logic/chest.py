import os
import random

import pygame
from pygame.rect import Rect

import logic.constants
from logic.load_image import load_image
from logic.particle import Particle

chest_group = pygame.sprite.Group()


class Chest(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y):
        super().__init__(chest_group)

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.add(chest_group)
        self.rect = self.image.get_rect().move(
            logic.constants.tile_width * pos_x, logic.constants.tile_height * pos_y)

        self.counter = 0
        self.cur_frame = 0
        self.coin_anim = []
        r_name = os.listdir(logic.constants.COIN_ANIM)
        for i in r_name:
            self.coin_anim.append(load_image(logic.constants.COIN_ANIM + i))
        self.particles = []

    def coin(self):
        if not(self.particles):
            numbers = range(-10, 10)
            for _ in range(50):
                start_anim = random.randint(0, len(self.coin_anim) - 1)
                par = Particle(self.rect.center, random.choice(numbers), random.choice(numbers),
                           self.coin_anim[start_anim])
                par.gravity = 0.07
                par.frame = start_anim
                self.particles.append(par)

    def update(self):
        for par in self.particles:
            par.frame = (par.frame + 1) % len(self.coin_anim)
            par.image = self.coin_anim[par.frame]
