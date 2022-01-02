from logic.imports import *
from logic.load_image import *
import logic.constants
from logic.term import terminate
from logic.buttons import Buttons
from logic.start_screen import *

# Код Рената --------------------------------------
def load_menu(screen, clock):
    btn_colors = [0, 0, 0]
    colors = logic.constants.BTN_COLOR
    center_pos = logic.constants.WIDTH // 2
    start_btn = Buttons('Начать', colors[btn_colors[0]], (center_pos, logic.constants.HEIGHT // 2))
    resume_btn = Buttons('Продолжить', colors[btn_colors[1]],
                         (center_pos, logic.constants.HEIGHT // 2 + start_btn.rect.height * 2))
    settings_btn = Buttons('Настройки', colors[btn_colors[2]],
                           (center_pos, logic.constants.HEIGHT // 2 + resume_btn.rect.height * 4))
    buttons = [start_btn, resume_btn, settings_btn]
    for button in buttons:
        screen.blit(button.text, (button.pos_x, button.pos_y))
    while True:
        screen.fill('black')
        fon = pygame.transform.scale(load_image(logic.constants.MENU_FON_PATH), (logic.constants.SIZE))
        screen.blit(fon, (0, 0))
        cursor_rect.center = pygame.mouse.get_pos()  # update position
        screen.blit(cursor, cursor_rect)
        for event in pygame.event.get():
            btn_colors = [0, 0, 0]
            if event.type == pygame.QUIT:
                terminate()
            try:
                for i, button in enumerate(buttons):
                    if button.rect.collidepoint(event.pos):
                        print(i)
                        btn_colors[i] = 1
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            return
            except AttributeError:
                pass

        start_btn = Buttons('Начать', colors[btn_colors[0]], (center_pos, logic.constants.HEIGHT // 2))
        resume_btn = Buttons('Продолжить', colors[btn_colors[1]],
                             (center_pos, logic.constants.HEIGHT // 2 + start_btn.rect.height * 2))
        settings_btn = Buttons('Настройки', colors[btn_colors[2]],
                               (center_pos, logic.constants.HEIGHT // 2 + resume_btn.rect.height * 4))
        buttons = [start_btn, resume_btn, settings_btn]
        for button in buttons:
            screen.blit(button.text, (button.pos_x, button.pos_y))
        clock.tick(logic.constants.FPS)
        pygame.display.flip()
