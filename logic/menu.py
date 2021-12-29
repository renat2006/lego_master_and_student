import pygame.mouse

from logic.imports import *
from logic.load_image import *
import logic.constants
from logic.term import terminate
from logic.buttons import Buttons


class Settings:
    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, 'red', (100, 100, logic.constants.WIDTH - 200, logic.constants.HEIGHT - 200), 10)
        pygame.draw.rect(self.screen, 'white', (105, 105, logic.constants.WIDTH - 210, logic.constants.HEIGHT - 210))


# Код Рената --------------------------------------
def load_menu(screen, clock):
    btn_colors = [0, 0, 0]
    settings = Settings(screen)
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

        for event in pygame.event.get():
            btn_colors = [0, 0, 0]
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                terminate()

            for i, button in enumerate(buttons):
                if button.rect.collidepoint(pygame.mouse.get_pos()):

                    btn_colors[i] = 1
                    if pygame.mouse.get_pressed()[0] and i == 0:
                        return

        start_btn = Buttons('Начать', colors[btn_colors[0]], (center_pos, logic.constants.HEIGHT // 2))
        resume_btn = Buttons('Продолжить', colors[btn_colors[1]],
                             (center_pos, logic.constants.HEIGHT // 2 + start_btn.rect.height * 2))
        settings_btn = Buttons('Настройки', colors[btn_colors[2]],
                               (center_pos, logic.constants.HEIGHT // 2 + resume_btn.rect.height * 4))

        buttons = [start_btn, resume_btn, settings_btn]
        for button in buttons:
            screen.blit(button.text, (button.pos_x, button.pos_y))

        #settings.draw()
        pygame.display.flip()
