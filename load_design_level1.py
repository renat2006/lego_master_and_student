import logic.load_image
import logic.constants
from generate_level import *
import pygame

#код Айгуль----------

def load_fon(fon_name, screen):
    fon = pygame.transform.scale(load_image(fon_name), logic.constants.SIZE)
    screen.fill("White")
    screen.blit(fon, (0, 0))


def load_level(filename):
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '-':
                Tile('plate', x, y)
            elif level[y][x] == '@':
                new_player = Player(logic.constants.PLAYER_IMAGE_PATH, (x, y))
    return new_player, x, y