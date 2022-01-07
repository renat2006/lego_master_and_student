import pygame.transform
import logic.constants

# код Айгуль--------


# группы спрайтов
from logic.load_image import load_image

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y):
        super().__init__(tiles_group)

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.add(tiles_group)
        self.rect = self.image.get_rect().move(
            logic.constants.tile_width * pos_x, logic.constants.tile_height * pos_y)

