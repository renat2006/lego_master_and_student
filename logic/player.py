import pygame

from logic.load_image import *
import logic.constants

# Код Димы--------------------------------------
player_group = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, sheet, columns, rows):
        super().__init__(player_group)
        self.idle = load_image(logic.constants.PLAYER_IMAGE_PATH)
        self.jump = load_image(logic.constants.PLAYER_JUMP_IMAGE_PATH)
        self.jump_fliped = pygame.transform.flip(load_image(logic.constants.PLAYER_JUMP_IMAGE_PATH), True, False)
        self.curr_jump = self.jump
        self.image = self.idle
        self.frames_normal = []
        self.frames_flipped = []

        r_name = os.listdir(logic.constants.PLAYER_RUN_IMAGE_PATH)
        for i in r_name:
            self.frames_normal.append(load_image(logic.constants.PLAYER_RUN_IMAGE_PATH + i))
        for i in r_name:
            self.frames_flipped.append(
                pygame.transform.flip(load_image(logic.constants.PLAYER_RUN_IMAGE_PATH + i), True, False))
        self.frames = self.frames_normal
        self.cur_frame = 0

        self.pos_x = x * logic.constants.player_width
        self.pos_y = y * logic.constants.player_height
        self.player_width = self.image.get_rect().width
        self.player_height = self.image.get_rect().height
        self.mask = pygame.mask.from_surface(self.image)

        self.jumping = False
        self.add(player_group)
        self.rect = self.image.get_rect().move(
            self.pos_x, self.pos_y)

    def link_to_surface(self, surface):
        self.screen = surface

    def move(self, x, y):
        if self.jumping is False:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def set_jump(self):
        if self.is_jump():
            self.jumping = False
        else:
            self.jumping = True

    def is_jump(self, jump=False):
        if self.jumping:
            self.image = self.curr_jump
            return True
        return False

    def next_jump_stage(self, jump_stage):
        self.rect = self.rect.move(0, jump_stage)

    def gravity(self):
        self.move(0, 9.8)

    def set_idle(self):
        self.image = self.idle
