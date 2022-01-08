def load_logic():
    keys = pygame.key.get_pressed()

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
                running = False

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
    if is_coll_chest:
        chest_group.sprites()[0].coin()