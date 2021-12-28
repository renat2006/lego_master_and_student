from logic.imports import *
from logic.screen_and_init import *
from logic.constants import *
screen = init(SIZE)
running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        screen.fill('black')

        pygame.display.flip()
