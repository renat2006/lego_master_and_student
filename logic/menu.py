from logic.imports import *
from logic.load_image import *
from logic.constants import *
from logic.term import terminate
from logic.buttons import Buttons


def load_menu(screen, clock):
    fon = pygame.transform.scale(load_image(MENU_FON_PATH), (SIZE))
    screen.blit(fon, (0, 0))
    start_btn = Buttons('Start', (255, 100, 100), (WIDTH // 2, HEIGHT // 2), screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                print(mouse_pos)

        pygame.display.flip()
        clock.tick(FPS)
