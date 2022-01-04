import pygame
from pygame.rect import Rect

import logic.constants
from logic.load_image import load_image


class Inventory:
    def __init__(self, screen):
        self.screen = screen
        self.padding = 5
        self.pos_x = (logic.constants.WIDTH - logic.constants.INVENTORY_COLUMNS * (
                logic.constants.INVENTORY_HEIGHT + self.padding) - self.padding) // 2
        self.pos_y = logic.constants.HEIGHT - logic.constants.INVENTORY_HEIGHT
        self.rect = Rect(self.pos_x, self.pos_y, logic.constants.INVENTORY_COLUMNS * (
                logic.constants.INVENTORY_HEIGHT + self.padding) + self.padding,
                         logic.constants.INVENTORY_HEIGHT)
        self.images = [load_image(logic.constants.tile_images['wall']), load_image(logic.constants.tile_images['plate'])]
        self.colors = ['black'] * logic.constants.INVENTORY_COLUMNS

    def draw(self, keys):
        pygame.draw.rect(self.screen, '#4f4f4f',
                         self.rect)
        if keys[pygame.K_1]:
            self.colors = ['black'] * logic.constants.INVENTORY_COLUMNS
            self.colors[0] = 'red'
        elif keys[pygame.K_2]:
            self.colors = ['black'] * logic.constants.INVENTORY_COLUMNS
            self.colors[1] = 'red'
        elif keys[pygame.K_3]:
            self.colors = ['black'] * logic.constants.INVENTORY_COLUMNS
            self.colors[2] = 'red'
        elif keys[pygame.K_4]:
            self.colors = ['black'] * logic.constants.INVENTORY_COLUMNS
            self.colors[3] = 'red'
        elif keys[pygame.K_5]:
            self.colors = ['black'] * logic.constants.INVENTORY_COLUMNS
            self.colors[4] = 'red'
        for i in range(logic.constants.INVENTORY_COLUMNS):
            curr_rect = pygame.draw.rect(self.screen, self.colors[i],
                                         (self.pos_x + self.padding + i * (
                                                 logic.constants.INVENTORY_HEIGHT + self.padding),
                                          self.pos_y + self.padding,
                                          logic.constants.INVENTORY_HEIGHT,
                                          logic.constants.INVENTORY_HEIGHT - self.padding * 2)
                                         )
            if i <= len(self.images) - 1:
                self.screen.blit(self.images[i],
                                 (curr_rect.x - self.images[i].get_rect().height // 2 + curr_rect.width // 2,
                                  curr_rect.y - self.images[i].get_rect().width // 2 + curr_rect.height // 2))
        if self.colors != ['black'] * logic.constants.INVENTORY_COLUMNS:
            return self.images[self.colors.index('red')]
        else:
            return False
