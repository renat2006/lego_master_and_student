import pygame.sprite

from generate_level import tiles_group, all_sprites
from load_design_level1 import load_fon, generate_level, load_level
from logic.screen_and_init import *
from logic.start_screen import *
from logic.menu import *
import logic.constants
from logic.player import *
from logic.in_game_menu import *

screen, clock = init(logic.constants.SIZE)
start_screen(screen, clock)
load_menu(screen, clock)
running = True
fon, moon = load_fon(logic.constants.BACKGROUND_1level, logic.constants.MOON_1level, screen)
player, level_x, level_y, tiles = generate_level(load_level('level1.txt'))
player.link_to_surface(screen)
jump_stage = logic.constants.JUMP_VALUE
jump_sound = pygame.mixer.Sound(logic.constants.JUMP_SOUND)
jump_sound.set_volume(pygame.mixer.music.get_volume() * 2)
inventoty = Inventory(screen)
while running:
    keys = pygame.key.get_pressed()

    player.set_idle()

    if keys[pygame.K_SPACE]:
        if not player.is_jump():
            jump_sound.play()
            player.set_jump()
    if player.is_jump():
        player.next_jump_stage(jump_stage)
        if jump_stage >= -logic.constants.JUMP_VALUE:
            player.set_jump()
            jump_stage = logic.constants.JUMP_VALUE
        else:

            jump_stage += 1

    if keys[pygame.K_RIGHT]:
        player.direction = 1
        if player.is_jump():
            player.move(logic.constants.STEP * 1.5, 0)

        else:
            player.move(logic.constants.STEP, 0)


    if keys[pygame.K_LEFT]:
        player.direction = -1
        if player.is_jump():
            player.move(-logic.constants.STEP * 1.5, 0)

        else:
            player.move(-logic.constants.STEP, 0)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            # if event.key == pygame.K_LEFT:
            #     player.move(-STEP, 0)
            # if event.key == pygame.K_RIGHT:
            #     player.move(STEP, 0)

    screen.fill('#202020')

    screen.blit(fon, (0, 0))
    block_texture = inventoty.draw(keys)
    tiles_group.draw(screen)
    tiles_group.update()
    player_group.draw(screen)
    if block_texture:
        if pygame.mouse.get_pressed()[0]:
            player.set_block(block_texture)
        player.draw_block(block_texture)


    clock.tick(60)
    pygame.display.flip()

# ------------------------------------------------------
