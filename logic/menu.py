from logic.imports import *
from logic.load_image import *
import logic.constants
from logic.term import terminate
from logic.buttons import Buttons


def load_menu(screen, clock):
    start_btn_color = (0, 0, 0)
    start_btn = Buttons('Start', start_btn_color, (logic.constants.WIDTH // 2, logic.constants.HEIGHT // 2))

    screen.blit(start_btn.text,
                (start_btn.pos_x, start_btn.pos_y))
    while True:
        screen.fill('black')
        fon = pygame.transform.scale(load_image(logic.constants.MENU_FON_PATH), (logic.constants.SIZE))

        screen.blit(fon, (0, 0))
        for event in pygame.event.get():
            start_btn_color = (0, 0, 0)
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
            try:
                if start_btn.rect.collidepoint(event.pos):
                    start_btn_color = (255, 0, 0)

            except AttributeError:
                pass

        start_btn = Buttons('Start', start_btn_color, (logic.constants.WIDTH // 2, logic.constants.HEIGHT // 2))

        screen.blit(start_btn.text,
                    (start_btn.pos_x, start_btn.pos_y))

        pygame.display.flip()
        clock.tick(logic.constants.FPS)
