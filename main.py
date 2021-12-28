from logic.screen_and_init import *
from logic.start_screen import *
from logic.menu import *
screen, clock = init(SIZE)
start_screen(screen, clock)
load_menu(screen, clock)
running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        screen.fill('black')
        clock.tick(FPS)
        pygame.display.flip()
