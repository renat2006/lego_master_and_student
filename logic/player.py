import pygame
from pygame.rect import Rect

from logic.load_image import *
import logic.constants
import sys

sys.path.insert(0, "../")
from generate_level import *

# Код Димы--------------------------------------
player_group = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(player_group)
        self.screen = None
        self.direction = 1
        self.idle = load_image(logic.constants.PLAYER_IMAGE_PATH)
        self.idle_flipped = pygame.transform.flip(load_image(logic.constants.PLAYER_IMAGE_PATH), True, False)
        self.jump = load_image(logic.constants.PLAYER_JUMP_IMAGE_PATH)
        self.jump_fliped = pygame.transform.flip(load_image(logic.constants.PLAYER_JUMP_IMAGE_PATH), True, False)
        self.image = self.idle
        self.frames_normal = []
        self.frames_flipped = []
        self.can_jump = True
        r_name = os.listdir(logic.constants.PLAYER_RUN_IMAGE_PATH)
        for i in r_name:
            self.frames_normal.append(load_image(logic.constants.PLAYER_RUN_IMAGE_PATH + i))
        for i in r_name:
            self.frames_flipped.append(
                pygame.transform.flip(load_image(logic.constants.PLAYER_RUN_IMAGE_PATH + i), True, False))

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

    def update(self, platform_list):
        self.platform_list = platform_list
        if not (self.jumping):
            self.gravity()

        block_hit_list = pygame.sprite.spritecollide(self, platform_list, False)
        if block_hit_list != []:

            for block in block_hit_list:

                if self.rect.top <= block.rect.top :
                    self.rect.bottom = block.rect.top
                    self.can_jump = True

        else:
            self.can_jump = False

    def link_to_surface(self, surface):
        self.screen = surface

    def move(self, x, y):

        self.rect = self.rect.move(x, y)
        block_hit_list = pygame.sprite.spritecollide(self, self.platform_list, False)
        for block in block_hit_list:
            if self.direction == 1 and self.rect.x <= block.rect.left:
                self.rect.right = block.rect.left

            elif self.direction == -1 and self.rect.x + self.image.get_width() >= block.rect.right:

                self.rect.left = block.rect.right
            print(self.rect.x, block.rect.right)

        if self.jumping is False:
            if self.direction == 1:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_normal)
                self.image = self.frames_normal[self.cur_frame]

            elif self.direction == -1:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_flipped)
                self.image = self.frames_flipped[self.cur_frame]

    def set_jump(self):
        if self.is_jump():
            self.jumping = False
        else:
            self.jumping = True

    def is_jump(self, jump=False):
        if self.jumping:
            if self.direction == 1:
                self.image = self.jump
            elif self.direction == -1:
                self.image = self.jump_fliped
            return True
        return False

    def next_jump_stage(self, jump_stage):
        self.rect = self.rect.move(0, jump_stage)

    def gravity(self):
        self.rect = self.rect.move(0, 9.8)

    def set_idle(self):
        if self.direction == 1:
            self.image = self.idle
        elif self.direction == -1:
            self.image = self.idle_flipped

    def draw_block(self, block_image):
        block_image = pygame.transform.scale(block_image, (block_image.get_height() // 3, block_image.get_width() // 3))
        self.block_rect = self.rect.right + 20, self.rect.top + (self.rect.height - block_image.get_height() // 3) // 2
        if self.direction == 1:
            self.screen.blit(block_image, self.block_rect
                             )
        elif self.direction == -1:
            self.screen.blit(block_image, self.block_rect)

    def set_block(self, block_image):
        self.block_rect = (
            self.rect.right + 20, self.rect.top + (self.rect.height - block_image.get_height() // 3) // 2)
        print(self.block_rect[0] // logic.constants.tile_width,
              self.block_rect[1] // logic.constants.tile_height)
        return Tile(block_image, self.block_rect[0] // logic.constants.tile_width,
                    self.block_rect[1] // logic.constants.tile_height)
