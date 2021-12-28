from logic.imports import *

FPS = 60



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
