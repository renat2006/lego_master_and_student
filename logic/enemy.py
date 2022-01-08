import os

import pygame
from logic.constants import *
from generate_level import *

enemy_group = pygame.sprite.Group()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(enemy_group)
        self.direction = RIGHT
        self.image = load_image(logic.constants.ENEMY_IMAGE_PATH)
        self.pos_x = x * enemy_width
        self.pos_y = y * enemy_height
        self.cur_frame = 0
        self.rect = self.image.get_rect().move(
            self.pos_x, self.pos_y)
        self.frames_normal = []
        r_name = os.listdir(logic.constants.ENEMY_RUN)
        for i in r_name:
            self.frames_normal.append(load_image(logic.constants.ENEMY_RUN + i))
        self.frames_flipped = []

        for i in r_name:
            self.frames_flipped.append(pygame.transform.flip(load_image(logic.constants.ENEMY_RUN + i), True, False))

    def link_to_surface(self, surface):
        self.screen = surface

    def set_direction(self):
        self.direction *= -1
        self.cur_frame = 0

    def move(self):
        self.rect = self.rect.move(ENEMY_STEP * self.direction, 0)
        if self.direction == 1:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames_normal)
            self.image = self.frames_normal[self.cur_frame]
        elif self.direction == -1:

            self.cur_frame = (self.cur_frame + 1) % len(self.frames_flipped)
            self.image = self.frames_flipped[self.cur_frame]

    def update(self):
        is_can_move = False
        for tile in tiles_group:
            if self.direction == RIGHT:
                if tile.rect.top == self.rect.bottom:
                    if tile.rect.left < self.rect.right + ENEMY_STEP <= tile.rect.right:
                        is_can_move = True
                if tile.rect.top < self.rect.bottom and tile.rect.bottom > self.rect.top:
                    if self.rect.right >= tile.rect.left > self.rect.left:
                        self.set_direction()
                        return
            if self.direction == LEFT:
                print(is_can_move)
                if tile.rect.top == self.rect.bottom:
                    if tile.rect.right > self.rect.left - ENEMY_STEP >= tile.rect.left:
                        is_can_move = True
                    else:
                        print(is_can_move)
                if tile.rect.top < self.rect.bottom and tile.rect.bottom > self.rect.top:
                    if self.rect.left <= tile.rect.right < self.rect.right:
                        self.set_direction()
                        return

        if is_can_move:
            self.move()
        else:
            self.set_direction()
        is_can_move = False
        # if is_down_way:
        #     print("yes")
        #     self.move()
        # else:
        #     self.set_direction()
        #
        # if tile.rect.top < self.rect.bottom and tile.rect.bottom > self.rect.top \
        #         and self.rect.left <= tile.rect.right and self.direction == LEFT:
        #     self.set_direction()
        #     return
        # if tile.rect.top < self.rect.bottom and tile.rect.bottom > self.rect.top \
        #         and self.rect.right >= tile.rect.left and self.direction == RIGHT:
        #     self.set_direction()
        #     print(2)
        #     return
