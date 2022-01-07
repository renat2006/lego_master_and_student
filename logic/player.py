import pygame
from pygame.rect import Rect
from logic.particle import *
from logic.load_image import *
import logic.constants
import sys
from logic.bullet import *

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
        self.gun = []
        self.can_jump = True
        self.shooting = False
        self.bullet_count = logic.constants.BULLET_COUNT
        self.block_count = logic.constants.BLOCK_COUNT
        self.up_boost_count = logic.constants.UP_BOOST_COUNT
        self.heart_count = logic.constants.HEART_COUNT
        self.speed_count = logic.constants.SPEED_COUNT
        self.counter = 0
        self.jump_boost = 1
        self.speed_boost = 1
        self.spell_timer = 0
        self.old_time = self.counter
        self.lives = 1
        self.live_image = pygame.transform.scale(load_image(logic.constants.HEART), (50, 50))
        r_name = os.listdir(logic.constants.PLAYER_RUN_IMAGE_PATH)
        for i in r_name:
            self.frames_normal.append(load_image(logic.constants.PLAYER_RUN_IMAGE_PATH + i))
        for i in r_name:
            self.frames_flipped.append(
                pygame.transform.flip(load_image(logic.constants.PLAYER_RUN_IMAGE_PATH + i), True, False))
        r_name = os.listdir(logic.constants.GUN_ANIM)
        for i in r_name:
            self.gun.append(load_image(logic.constants.GUN_ANIM + i))
        self.cur_frame = 0
        self.cur_gun_frame = 0
        self.pos_x = x * logic.constants.player_width
        self.pos_y = y * logic.constants.player_height
        self.player_width = self.image.get_rect().width
        self.player_height = self.image.get_rect().height
        self.mask = pygame.mask.from_surface(self.image)

        self.jumping = False
        self.add(player_group)
        self.rect = self.image.get_rect().move(
            self.pos_x, self.pos_y)

    def spell_check(self):
        if self.jump_boost == 2 or self.speed_boost == 2:
            font = pygame.font.Font(logic.constants.FONT_PATH, logic.constants.MAIN_TEXT_SIZE)
            text = font.render(str(15 - self.spell_timer // logic.constants.FPS), True, 'red')
            self.screen.blit(text, (logic.constants.WIDTH // 2 - text.get_width() // 2, 100))
            self.spell_timer += 1
        if self.spell_timer >= 15 * logic.constants.FPS:
            self.spell_timer = 0
            self.jump_boost = 1
            self.speed_boost = 1

    def update(self, platform_list):

        self.platform_list = platform_list
        if not self.jumping:
            self.gravity()

        block_hit_list = pygame.sprite.spritecollide(self, platform_list, False)
        if block_hit_list:

            for block in block_hit_list:

                if self.rect.bottom >= block.rect.top > self.rect.top:
                    self.rect.bottom = block.rect.top
                    self.can_jump = True

                if block.rect.bottom >= self.rect.top > block.rect.top:
                    self.rect.top = block.rect.bottom

        else:
            self.can_jump = False

        if self.counter - self.old_time >= 7:
            self.counter = 7
        else:
            self.counter += 1

    def link_to_surface(self, surface):
        self.screen = surface

    def move(self, x, y):

        self.rect = self.rect.move(x * self.speed_boost, y)
        block_hit_list = pygame.sprite.spritecollide(self, self.platform_list, False)
        for block in block_hit_list:
            if self.direction == logic.constants.RIGHT and self.rect.left <= block.rect.left:
                self.rect.right = block.rect.left

            elif self.direction == logic.constants.LEFT and self.rect.x + self.rect.width >= block.rect.right:
                self.rect.left = block.rect.right

        if not self.jumping:
            if self.direction == logic.constants.RIGHT:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_normal)
                self.image = self.frames_normal[self.cur_frame]

            elif self.direction == logic.constants.LEFT:
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
        self.rect = self.rect.move(0, jump_stage * self.jump_boost)

    def gravity(self):
        self.rect = self.rect.move(0, 9.8 * self.jump_boost)

    def set_idle(self):
        if self.direction == 1:
            self.image = self.idle
        elif self.direction == -1:
            self.image = self.idle_flipped

    def lives_manager(self):

        for i in range(self.lives):
            self.screen.blit(self.live_image, ((5 + self.live_image.get_width()) * i + 10, 25))

    def draw_block(self, block_image, block_id):
        self.block_id = block_id
        font = pygame.font.Font(logic.constants.FONT_PATH, 20)
        if block_image == logic.constants.GUN:

            text = font.render(str(self.bullet_count), True, 'red')

            if self.shooting:
                self.cur_gun_frame = (self.cur_gun_frame + 1) % len(self.gun)

            if self.cur_gun_frame + 1 == len(self.gun):
                self.shooting = False
            if self.direction == 1:
                self.block_rect = self.rect.right, self.rect.top + self.rect.height // 4

                block_image = self.gun[self.cur_gun_frame]
            elif self.direction == -1:
                self.block_rect = self.rect.left - self.rect.width, self.rect.top + self.rect.height // 4
                block_image = pygame.transform.flip(self.gun[self.cur_gun_frame], True, False)
            text_rect = self.block_rect[0] + 25, self.block_rect[1] - font.get_height()


        else:

            if self.direction == 1:
                block_image = pygame.transform.scale(block_image,
                                                     (block_image.get_width() // 3, block_image.get_height() // 3))
                self.block_rect = self.rect.right + 20, self.rect.top + (
                        self.rect.height - block_image.get_height() // 3) // 2
            elif self.direction == -1:
                block_image = pygame.transform.scale(block_image,
                                                     (block_image.get_height() // 3, block_image.get_width() // 3))
                block_image = pygame.transform.flip(block_image, True, False)
                self.block_rect = self.rect.left - 20, self.rect.top + (
                        self.rect.height - block_image.get_height() // 3) // 2
            print(block_id)
            if block_id == 0:
                text = font.render(str(self.block_count), True, 'red')
            elif block_id == 1:
                text = font.render(str(self.up_boost_count), True, 'red')
            elif block_id == 2:
                text = font.render(str(self.speed_count), True, 'red')
            elif block_id == 3:
                text = font.render(str(self.heart_count), True, 'red')
            text_rect = self.block_rect[0] + block_image.get_width() // 2, self.block_rect[1] - font.get_height()

        self.screen.blit(text, text_rect)
        self.screen.blit(block_image, self.block_rect)

    def set_block(self, block_image):
        if block_image != logic.constants.GUN:
            time_check = self.counter % 7 == 0 and self.spell_timer == 0
            self.block_rect = (
                self.rect.right + 20, self.rect.top + (self.rect.height - block_image.get_height() // 3) // 2)
            if self.block_id == 1 and time_check and self.up_boost_count > 0:

                self.up_boost_count -= 1
                self.jump_boost = 2
                numbers = range(-10, 10)
                for _ in range(20):
                    Particle(self.block_rect, random.choice(numbers), random.choice(numbers), block_image)
            elif self.block_id == 2 and time_check and self.speed_count > 0:

                self.speed_count -= 1
                self.speed_boost = 2
                numbers = range(-10, 10)
                for _ in range(20):
                    Particle(self.block_rect, random.choice(numbers), random.choice(numbers), block_image)
            elif self.block_id == 3 and time_check and self.heart_count > 0:

                self.heart_count -= 1
                self.lives += 1
                numbers = range(-10, 10)
                for _ in range(20):
                    Particle(self.block_rect, random.choice(numbers), random.choice(numbers), block_image)
            elif self.block_id == 0 and time_check and self.block_count > 0:

                self.block_count -= 1
                return Tile(block_image, self.block_rect[0] // logic.constants.tile_width,
                            self.block_rect[1] // logic.constants.tile_height)
            self.old_time = self.counter

        else:
            if self.counter % 7 == 0 and self.bullet_count > 0:
                if block_image == logic.constants.GUN:
                    Bullet(self.block_rect[0], self.block_rect[1] + 12, 50 * self.direction)
                    self.shooting = True
                    self.bullet_count -= 1
                self.old_time = self.counter
            return None
