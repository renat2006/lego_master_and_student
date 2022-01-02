from logic.imports import *
from logic.load_image import *
from logic.term import *
import logic.constants


cursor = load_image(logic.constants.CURSOR_IMG)
cursor_rect = cursor.get_rect()
# Код Рената --------------------------------------
def start_screen(screen, clock):
    intro_text = ['']

    fon = pygame.transform.scale(load_image(logic.constants.INTRO_FON_PATH), (logic.constants.SIZE))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    pygame.mouse.set_visible(False)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        cursor_rect.center = pygame.mouse.get_pos()  # update position
        screen.blit(fon, (0, 0))
        screen.blit(cursor, cursor_rect)
        pygame.display.flip()
        clock.tick(logic.constants.FPS)
