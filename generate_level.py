from logic.player import *
import logic.constants

#код Айгуль--------

player = pygame.image.load(logic.constants.PLAYER_IMAGE_PATH)
player_image = pygame.transform.scale(player, (70, 70))

# основной персонаж
player = None

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        try:
            self.image = pygame.image.load(logic.constants.tile_images[tile_type])
            self.rect = self.image.get_rect().move(
                logic.constants.tile_width * pos_x, logic.constants.tile_height * pos_y)
        except Exception:
            pass

