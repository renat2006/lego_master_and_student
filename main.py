import importlib
import pygame.sprite
from generate_level import tiles_group, all_sprites

from logic.camera import Camera
from logic.database import update_table, select_table
from logic.final import final_screen

from logic.screen_and_init import *
from logic.start_screen import *
from logic.menu import *
import logic.constants
from logic.chest import chest_group
from load_design_level1 import load_fon, generate_level, load_level
from logic.player import *
from logic.in_game_menu import *
from logic.loot import *
from logic.enemy import enemy_group
import cv2

screen, clock = init(logic.constants.SIZE)

start_screen(screen, clock)
load_menu(screen, clock)


def video(number):
    cap = cv2.VideoCapture(f'data/video/{number}.mp4')
    success, img = cap.read()
    shape = img.shape[1::-1]
    wn = pygame.display.set_mode(shape)
    clock = pygame.time.Clock()

    while success:
        clock.tick(50)
        success, img = cap.read()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                success = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
        try:
            wn.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))
        except AttributeError:
            return
        pygame.display.update()


def main(level):
    running = True
    fon = load_fon(logic.constants.FONS[level], screen)
    player, level_x, level_y, tiles, enemy = generate_level(load_level(f'level{level}.txt'))
    player.link_to_surface(screen)
    jump_stage = logic.constants.JUMP_VALUE
    jump_sound = pygame.mixer.Sound(logic.constants.JUMP_SOUND)
    jump_sound.set_volume(pygame.mixer.music.get_volume() * 2)
    inventory = Inventory(screen)
    is_collide = False
    camera = Camera()
    while running:
        keys = pygame.key.get_pressed()
        if player.lives == 0:
            main(level)
            return
        player.set_idle()
        player_group.update(tiles_group)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.direction = 1
            if player.is_jump():
                player.move(logic.constants.STEP * 1.5, 0)

            else:
                player.move(logic.constants.STEP, 0)

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.direction = -1
            if player.is_jump():
                player.move(-logic.constants.STEP * 1.5, 0)

            else:
                player.move(-logic.constants.STEP, 0)
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            if not player.is_jump() and player.can_jump:
                jump_sound.play()
                player.set_jump()
        if player.is_jump():
            player.next_jump_stage(jump_stage)
            if jump_stage >= -logic.constants.JUMP_VALUE:
                player.set_jump()
                jump_stage = logic.constants.JUMP_VALUE
            else:

                jump_stage += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()

        screen.fill('#202020')

        screen.blit(fon, (0, 0))
        block_texture, block_id = inventory.draw(keys)
        tiles_group.draw(screen)
        tiles_group.update()
        player_group.draw(screen)
        bullet_group.update()
        bullet_group.draw(screen)
        particle_group.update()
        particle_group.draw(screen)
        loot_group.update()
        loot_group.draw(screen)
        enemy_group.update()
        enemy_group.draw(screen)
        pygame.sprite.groupcollide(bullet_group, tiles_group, True, True)
        player.spell_check()
        player.lives_manager()
        chest_group.update()
        camera.update(player)
        collide_enemy = pygame.sprite.spritecollide(player, enemy_group, False)
        if collide_enemy:
            if player.is_jump():
                player.set_jump()
                jump_stage = JUMP_VALUE
            player.collide_with_enemy(collide_enemy)

        chest_group.draw(screen)
        loot_list_hit = pygame.sprite.spritecollide(player, loot_group, False)
        for loot in loot_list_hit:
            numbers = range(-10, 10)
            for _ in range(100):
                Particle(loot.rect.center, random.choice(numbers), random.choice(numbers), loot.image)
            if loot.bonus_effect == 'speed':
                player.speed_count += 1
            elif loot.bonus_effect == 'live':
                player.heart_count += 1
            elif loot.bonus_effect == 'jump':
                player.up_boost_count += 1
            loot.kill()
        if block_texture:
            can_build = True
            if keys[pygame.K_f] or keys[pygame.K_s] or keys[pygame.K_DOWN]:
                if block_id != 0:
                    block = player.set_block(block_texture)
                for block in tiles_group:
                    if block.rect.x <= player.rect.right + 20 < block.rect.right \
                            and player.rect.bottom > block.rect.top and player.rect.top < block.rect.bottom:
                        print(False)
                        can_build = False
                if can_build and block_id == 0:
                    block = player.set_block(block_texture)
                    tiles.append(block)
                elif player.bullet_count == 0:
                    new_anim = [load_image(logic.constants.GUN_ANIM_RELOAD + i) for i in
                                os.listdir(logic.constants.GUN_ANIM_RELOAD)]
                    inventory.gun = new_anim

            player.draw_block(block_texture, block_id)
        is_coll_chest = pygame.sprite.spritecollide(player, chest_group, False)
        collide_enemy = pygame.sprite.spritecollide(player, enemy_group, False)
        if collide_enemy:
            if player.is_jump():
                player.set_jump()
                jump_stage = logic.constants.JUMP_VALUE
            player.collide_with_enemy(collide_enemy)
        if is_coll_chest:
            chest_group.sprites()[0].coin()
            player.points += 10
            player.jump_boost = 0
            player.speed_boost = 0
            if not particle_group.sprites():
                update_table('points', 'points', player.points, 'id', 1)
                for sprite in player_group:
                    sprite.kill()
                for sprite in tiles_group:
                    sprite.kill()
                for sprite in loot_group:
                    sprite.kill()
                for sprite in chest_group:
                    sprite.kill()
                for sprite in enemy_group:
                    sprite.kill()
                for sprite in particle_group:
                    sprite.kill()

                return

        if player.lives <= 0 or player.down_check():

            for sprite in player_group:
                sprite.kill()
            for sprite in tiles_group:
                sprite.kill()
            for sprite in loot_group:
                sprite.kill()
            for sprite in chest_group:
                sprite.kill()
            for sprite in enemy_group:
                sprite.kill()
            for sprite in particle_group:
                sprite.kill()
            main(level)
            return
        for sprite in player_group:
            camera.apply(sprite)
        for sprite in tiles_group:
            camera.apply(sprite)
        for sprite in loot_group:
            camera.apply(sprite)
        for sprite in chest_group:
            camera.apply(sprite)
        for sprite in enemy_group:
            camera.apply(sprite)
        for sprite in particle_group:
            camera.apply(sprite)
        clock.tick(logic.constants.FPS)
        pygame.display.flip()


if int(select_table('current_level', 'curr_level')[0][0]) == 1:
    update_table('points', 'points', 0, 'id', 1)
    update_table('current_level', 'curr_level', 1, 'id', 1)
    update_table('current_level', 'level_name', 2, 'id', 1)
    video('1')
    main('1')
    update_table('current_level', 'curr_level', 2, 'id', 1)
    update_table('current_level', 'level_name', 2, 'id', 1)
if int(select_table('current_level', 'curr_level')[0][0]) == 2:
    video('2')
    main('2')
    update_table('current_level', 'curr_level', 3, 'id', 1)
    update_table('current_level', 'level_name', 3, 'id', 1)
if int(select_table('current_level', 'curr_level')[0][0]) == 3:
    video('3')
    main('3')
    update_table('current_level', 'curr_level', 1, 'id', 1)
    update_table('current_level', 'level_name', 2, 'id', 1)
    final_screen(screen, clock, *select_table('points', 'points'))
