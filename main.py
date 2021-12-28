from logic.screen_and_init import *
from logic.start_screen import *
from logic.menu import *
import logic.constants
from logic.player import *

screen, clock = init(logic.constants.SIZE)
start_screen(screen, clock)
load_menu(screen, clock)
running = True


def jump(obj):
    space = -15
    while space <= 15:
        obj.move(0, space)
        space += 1
        screen.fill("Black")
        screen.fill("White", (0, 500, logic.constants.WIDTH, 10))
        obj.update()
        player_group.draw(screen)
        pygame.time.delay(40)

        pygame.display.flip()


def main():
    pygame.display.set_caption("Движение")

    player = Player("data/player.png", (5, 400))

    running = True
    while running:
        spaces = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jump(player)
                if event.key == pygame.K_LEFT:
                    player.move(-logic.constants.STEP, 0)
                if event.key == pygame.K_RIGHT:
                    player.move(logic.constants.STEP, 0)

        screen.fill("Black")
        screen.fill("White", (0, 500, logic.constants.WIDTH, 10))
        player_group.update()
        player_group.draw(screen)

        pygame.display.flip()

    pygame.quit()


while running:
    for event in pygame.event.get():
        main()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        screen.fill('black')
        clock.tick(logic.constants.FPS)
        pygame.display.flip()
