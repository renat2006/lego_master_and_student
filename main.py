from logic.screen_and_init import *
from logic.start_screen import *
from logic.menu import *
import logic.constants
from logic.player import *
from load_design_level1 import *

screen, clock = init(logic.constants.SIZE)
start_screen(screen, clock)
load_menu(screen, clock)
player_image = load_image(logic.constants.PLAYER_IMAGE_PATH)


running = True
jumping = False
player, level_x, level_y = generate_level(load_level('level1.txt'))


# Код Димы ------------------------------------
def jump(obj):
    space = -15
    while space <= 15:
        obj.move(0, space)
        space += 1
        screen.fill("Black")
        screen.fill("White", (0, 500, logic.constants.WIDTH, 10))
        obj.update()
        player_group.draw(screen)
        pygame.time.delay(20)

        pygame.display.flip()
#-------------------------------------------------

# Код Рената --------------------------------------

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            # Код Димы --------------------------------------
            if event.key == pygame.K_SPACE:
                jump(player)

            if event.key == pygame.K_LEFT:
                player.move(-logic.constants.STEP, 0)
            if event.key == pygame.K_RIGHT:
                player.move(logic.constants.STEP, 0)

    load_fon(logic.constants.BACKGROUND_1level, screen)
    cursor_rect.center = pygame.mouse.get_pos()  # update position
    screen.blit(cursor, cursor_rect)

    all_sprites.draw(screen)
    all_sprites.update()
    player_group.draw(screen)
    player_group.update()
    tiles_group.draw(screen)
    tiles_group.update()

    pygame.display.flip()

pygame.quit()

#------------------------------------------------------