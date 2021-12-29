import pygame

from logic.load_image import *
from logic.constants import PLAYER_IMAGE_PATH, JUMP_VALUE, STEP

# Код Димы--------------------------------------
player_group = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(player_group)
        self.image = load_image(PLAYER_IMAGE_PATH, -1)
        self.clock = pygame.time.Clock()

        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.player_width = self.image.get_rect().width
        self.player_height = self.image.get_rect().height
        self.rect = self.image.get_rect().move(
            self.pos_x, self.pos_y)

        self.jumping = False

    def link_to_surface(self, surface):
        self.screen = surface

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def set_jump(self):
        if self.is_jump():
            self.jumping = False
        else:
            self.jumping = True

    def is_jump(self, jump=False):
        if self.jumping:
            return True
        return False

    def next_jump_stage(self, jump_stage):
        self.move(0, jump_stage)
        pygame.time.delay(10)

        # while space <= 15:
        #     obj.move(0, space)
        #     space += 1
        #     screen.fill("Black")
        #     screen.fill("White", (0, 500, logic.constants.WIDTH, 10))
        #     obj.update()
        #     player_group.draw(screen)
        #     pygame.time.delay(20)
