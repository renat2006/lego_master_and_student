from logic.screen_and_init import *
from logic.start_screen import *
from logic.menu import *
import logic.constants
from logic.player import *

screen, clock = init(logic.constants.SIZE)
start_screen(screen, clock)
load_menu(screen, clock)
running = True
player = Player((5, 400))


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


# -------------------------------------------------

# Код Рената --------------------------------------
jump_stage = JUMP_VALUE
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                if not player.is_jump():
                    player.set_jump()
            if event.key == pygame.K_LEFT:
                player.move(-logic.constants.STEP, 0)
            if event.key == pygame.K_RIGHT:
                player.move(logic.constants.STEP, 0)
    if player.is_jump():
        player.next_jump_stage(jump_stage)
        if jump_stage >= -JUMP_VALUE:
            player.set_jump()
            jump_stage = JUMP_VALUE
        else:
            jump_stage += 1
    screen.fill('black')
    screen.fill("White", (0, 500, logic.constants.WIDTH, 10))

    player_group.update()
    player_group.draw(screen)
    clock.tick(logic.constants.FPS)
    pygame.display.flip()

# ------------------------------------------------------
