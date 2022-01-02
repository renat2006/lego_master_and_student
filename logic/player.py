import logic.constants
from logic.load_image import *
from generate_level import player_group

# Код Димы--------------------------------------

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

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
