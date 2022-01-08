import random

import pygame
from pygame.rect import Rect
import logic.constants

from logic.load_image import load_image

particle_group = pygame.sprite.Group()


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера


    def __init__(self, pos, dx, dy, image):
        self.fire = [image]
        for scale in (5, 10, 20):
            self.fire.append(pygame.transform.scale(self.fire[0], (scale, scale)))
        super().__init__(particle_group)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        self.velocity = [dx, dy]

        self.rect.x, self.rect.y = pos

        self.gravity = 0.2

    def update(self):

        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if not self.rect.colliderect(Rect(0, 0, logic.constants.WIDTH, logic.constants.HEIGHT)):
            self.kill()
