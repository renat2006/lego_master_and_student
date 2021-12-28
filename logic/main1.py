import pygame
from player import Player, player_group
from constants import SIZE, FPS, WIDTH, STEP

screen = pygame.display.set_mode(SIZE)
pygame.display.set_mode(SIZE)


def jump(obj):
    space = -15
    while space <= 15:
        obj.move(0, space)
        space += 1
        screen.fill("Black")
        screen.fill("White", (0, 500, WIDTH, 10))
        obj.update()
        player_group.draw(screen)
        pygame.time.delay(40)

        pygame.display.flip()


def main():
    pygame.display.set_caption("Движение")
    clock = pygame.time.Clock()

    player = Player("../data/player.png", (5, 400))

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
                    player.move(-STEP, 0)
                if event.key == pygame.K_RIGHT:
                    player.move(STEP, 0)

        screen.fill("Black")
        screen.fill("White", (0, 500, 1443, 10))
        player_group.update()
        player_group.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
