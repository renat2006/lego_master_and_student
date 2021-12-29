import logic.load_image
import logic.constants
from generate_level import *


#код Айгуль----------

def load_fon():
    pygame.transform.scale(load_image('fon.jpg'), (logic.constants.WIDTH, logic.constants.HEIGHT))


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
                new_player = Player(x, y)
    return new_player, x, y
