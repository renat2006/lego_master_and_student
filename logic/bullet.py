import pygame

from logic.load_image import load_image
import logic.constants

bullet_group = pygame.sprite.Group()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed):
        super().__init__(bullet_group)

        self.image = load_image(logic.constants.BULLET)

        self.add(bullet_group)
        self.rect = self.image.get_rect().move(
            pos_x, pos_y)
        self.speed = speed
    def update(self):
        self.rect = self.rect.move(self.speed, 0)
        if self.rect.x > logic.constants.WIDTH or self.rect.x < 0:
            self.kill()
