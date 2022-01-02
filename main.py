from generate_level import tiles_group, all_sprites
from load_design_level1 import load_fon, generate_level, load_level
from logic.screen_and_init import *
from logic.start_screen import *
from logic.menu import *
import logic.constants
from logic.player import *

screen, clock = init(logic.constants.SIZE)
start_screen(screen, clock)
load_menu(screen, clock)
running = True

player, level_x, level_y = generate_level(load_level('level1.txt'))
jump_stage = logic.constants.JUMP_VALUE
while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if player.is_jump():
            player.move(-logic.constants.STEP * 5, 0)
        else:
            player.move(-logic.constants.STEP, 0)
    if keys[pygame.K_RIGHT]:
        if player.is_jump():
            player.move(logic.constants.STEP * 5, 0)
        else:
            player.move(logic.constants.STEP, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                if not player.is_jump():
                    player.set_jump()
            # if event.key == pygame.K_LEFT:
            #     player.move(-STEP, 0)
            # if event.key == pygame.K_RIGHT:
            #     player.move(STEP, 0)
    if player.is_jump():
        player.next_jump_stage(jump_stage)
        if jump_stage >= -logic.constants.JUMP_VALUE:
            player.set_jump()
            jump_stage = logic.constants.JUMP_VALUE
        else:
            jump_stage += 1
    screen.fill('black')
    screen.fill("White", (0, 500, logic.constants.WIDTH, 10))

    load_fon(logic.constants.BACKGROUND_1level, screen)

    all_sprites.draw(screen)
    all_sprites.update()
    tiles_group.draw(screen)
    tiles_group.update()
    player_group.draw(screen)
    player_group.update()
    pygame.display.flip()
    if player.is_jump():
        clock.tick(60)
    else:
        clock.tick(logic.constants.FPS)

# ------------------------------------------------------
