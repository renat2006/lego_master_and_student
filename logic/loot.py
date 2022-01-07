import pygame
import logic.constants
from logic.particle import Particle

loot_group = pygame.sprite.Group()


class Loot(pygame.sprite.Sprite):
    def __init__(self, image, bonus, pos_x, pos_y):
        super().__init__(loot_group)

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.add(loot_group)
        self.rect = self.image.get_rect().move(
            logic.constants.tile_width * pos_x, logic.constants.tile_height * pos_y)
        self.bonus_effect = bonus
        self.counter = 0

    def particle(self):
        numbers = range(-10, 10)
        for _ in range(20):
            Particle(self.block_rect, random.choice(numbers), random.choice(numbers), block_image)
