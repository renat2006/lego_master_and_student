import pygame
from logic.player import *
import logic.constants

#код Айгуль--------
player_image = load_image(logic.constants.PLAYER_IMAGE_PATH)

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        try:
            self.image = logic.constants.tile_images[tile_type]
        except Exception:
            pass
        self.rect = self.image.get_rect().move(
            logic.constants.tile_width * pos_x, logic.constants.tile_height * pos_y)