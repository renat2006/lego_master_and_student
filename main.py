from logic.screen_and_init import *
from logic.start_screen import *
from logic.menu import *
import logic.constants
from logic.player import *

screen, clock = init(logic.constants.SIZE)
start_screen(screen, clock)
load_menu(screen, clock)
running = True
jumping = False
player = Player("data/player.png", (5, 400))

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
    screen.fill('black')

    screen.fill("White", (0, 500, logic.constants.WIDTH, 10))

    player_group.draw(screen)
    player_group.update()
    all_sprites.draw(screen)
    clock.tick(logic.constants.FPS)
    pygame.display.flip()

#------------------------------------------------------