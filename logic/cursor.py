import pygame
from pygame.rect import Rect

from logic.load_image import load_image
import logic.constants


def set_cursor():
    cursor_img = load_image(logic.constants.CURSOR_PATH)
    pygame.mouse.set_visible(False)
    cursor_img = pygame.transform.scale(cursor_img, (cursor_img.get_width() * logic.constants.SCREEN_CONST,
                                  cursor_img.get_height() * logic.constants.SCREEN_CONST))
    cursor_img_rect = cursor_img.get_rect()

    return cursor_img, cursor_img_rect
