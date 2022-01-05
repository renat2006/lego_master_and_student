import logic.load_image
import logic.constants
from generate_level import *
import pygame
from logic.player import *


# код Айгуль----------

def load_fon(fon_name, moon_name, screen):
    fon = pygame.transform.scale(load_image(fon_name), logic.constants.SIZE)
    moon = pygame.transform.scale(load_image(moon_name), logic.constants.SIZE)
    return fon, moon


def load_level(filename):
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):
    new_player, x, y, tiles = None, None, None, []
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '#':
                tiles.append(Tile(load_image(logic.constants.tile_images['wall']), x, y))
            elif level[y][x] == '-':
                tiles.append(Tile(load_image(logic.constants.tile_images['plate']), x, y))
            elif level[y][x] == '@':
                new_player = Player(x, y)
                print(x, y)
    return new_player, x, y, tiles
