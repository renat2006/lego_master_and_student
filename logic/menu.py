import pygame.mouse

from logic.imports import *
from logic.load_image import *
import logic.constants
from logic.screen_and_init import init
from logic.term import terminate
from logic.buttons import Buttons
from pygame_textinput import *
from pygame.rect import Rect
from logic.text import *
from logic.sett_fon import *
from logic.input_field import *
from logic.cursor import set_cursor

class Settings:
    def __init__(self, screen):
        self.screen = screen
        self.set_fon = Settings_fon(self.screen,
                                    (105 * logic.constants.SCREEN_CONST, 105 * logic.constants.SCREEN_CONST),
                                    (logic.constants.WIDTH - 210 * logic.constants.SCREEN_CONST,
                                     logic.constants.HEIGHT - 210 * logic.constants.SCREEN_CONST), 'white')

        pygame.key.set_repeat(200, 25)

        self.input_fields = [Input_Field(logic.constants.HEADING_FONT_SIZE, 'blue', 4, 400, 'blue',
                                         (self.set_fon.rect.width // 1.5,
                                          self.set_fon.rect.y + 150),
                                         "(input.isnumeric() and 0 < int(input) <= logic.constants.WIDTH) or input == ''",
                                         logic.constants.WIDTH),
                             Input_Field(logic.constants.HEADING_FONT_SIZE, 'blue', 4, 400, 'blue',
                                         (self.set_fon.rect.width // 1.2,
                                          self.set_fon.rect.y + 150),
                                         "(input.isnumeric() and 0 < int(input) <= logic.constants.HEIGHT) or input == ''",
                                         logic.constants.HEIGHT)
                             ]

        self.settings_texts = [
            Text('Настройки', logic.constants.HEADING_FONT_SIZE, (logic.constants.WIDTH // 2, self.set_fon.rect.y + 50),
                 'black'),
            Text('Размеры Окна', logic.constants.MAIN_TEXT_SIZE,
                 (self.set_fon.rect.x + 200,
                  self.set_fon.rect.y + 150),
                 'black'),
            Text('x', logic.constants.MAIN_TEXT_SIZE, (self.input_fields[0].border_rect.right + (
                    self.input_fields[1].border_rect.x - self.input_fields[
                0].border_rect.right) // 2,
                                                       self.input_fields[0].rect.y + self.input_fields[
                                                           0].rect.height // 2),
                 'blue')

        ]
        self.settings_buttons = [
            Buttons('Применить', 'black',
                    (logic.constants.WIDTH // 2, self.set_fon.rect.bottom - 50 * logic.constants.SCREEN_CONST))

        ]

    def draw(self):
        self.set_fon.draw()

        for text in self.settings_texts:
            self.screen.blit(text.text, text.rect)

        for input_field in self.input_fields:
            self.screen.blit(input_field.textinput.surface, input_field.rect)
            pygame.draw.rect(self.screen, 'red', input_field.border_rect, int(5 * logic.constants.SCREEN_CONST))
        for button in self.settings_buttons:
            self.screen.blit(button.text, (button.pos_x, button.pos_y))


# Код Рената --------------------------------------
def load_menu(screen, clock):
    cursor,  cursor_img_rect = set_cursor()

    btn_colors = [0, 0, 0]
    logo_image = pygame.transform.scale(load_image(logic.constants.LOGO_PATH),
                                        (logic.constants.LOGO_SIZE[0] * logic.constants.SCREEN_CONST,
                                         logic.constants.LOGO_SIZE[1] * logic.constants.SCREEN_CONST))
    settings = Settings(screen)
    settings.draw()
    colors = logic.constants.BTN_COLOR
    center_pos = logic.constants.WIDTH // 2
    logo_center = logo_image.get_rect(center=(center_pos, logic.constants.HEIGHT // 3))
    start_btn = Buttons('Начать', colors[btn_colors[0]], (center_pos, logic.constants.HEIGHT // 2))
    resume_btn = Buttons('Продолжить', colors[btn_colors[1]],
                         (center_pos, logic.constants.HEIGHT // 2 + start_btn.rect.height * 2))
    settings_btn = Buttons('Настройки', colors[btn_colors[2]],
                           (center_pos, logic.constants.HEIGHT // 2 + resume_btn.rect.height * 4))
    buttons = [start_btn, resume_btn, settings_btn]

    is_opened_set = False
    active_input_field = 0
    for button in buttons:
        screen.blit(button.text, (button.pos_x, button.pos_y))

    while True:
        screen.fill('white')
        screen.blit(logo_image, logo_center)
        cursor_img_rect.center = pygame.mouse.get_pos()

        events = pygame.event.get()
        settings.input_fields[active_input_field].textinput.update(events)

        for event in events:
            btn_colors = [0, 0, 0]
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                terminate()

            for i, button in enumerate(buttons):
                if button.rect.collidepoint(pygame.mouse.get_pos()):

                    btn_colors[i] = 1
                    if pygame.mouse.get_pressed()[0] and i == 0:
                        return
                    elif pygame.mouse.get_pressed()[0] and i == 2:
                        is_opened_set = True

            for i, field in enumerate(settings.input_fields):
                if field.rect.collidepoint(pygame.mouse.get_pos()):

                    if pygame.mouse.get_pressed()[0]:
                        active_input_field = i
            for i, button in enumerate(settings.settings_buttons):
                if button.rect.collidepoint(pygame.mouse.get_pos()):

                    if pygame.mouse.get_pressed()[0] and i == 0:
                        logic.constants.SIZE = logic.constants.WIDTH, logic.constants.HEIGHT = (int(
                            settings.input_fields[
                                0].textinput.value),
                                                                                                int(
                                                                                                    settings.input_fields[
                                                                                                        1].textinput.value))

                        logic.screen_and_init.init(logic.constants.SIZE)
                        load_menu(screen, clock)
                        return

        start_btn = Buttons('Начать', colors[btn_colors[0]], (center_pos, logic.constants.HEIGHT // 2))
        resume_btn = Buttons('Продолжить', colors[btn_colors[1]],
                             (center_pos, logic.constants.HEIGHT // 2 + start_btn.rect.height * 2))
        settings_btn = Buttons('Настройки', colors[btn_colors[2]],
                               (center_pos, logic.constants.HEIGHT // 2 + resume_btn.rect.height * 4))

        buttons = [start_btn, resume_btn, settings_btn]
        for button in buttons:
            screen.blit(button.text, (button.pos_x, button.pos_y))
        if is_opened_set:
            settings.draw()
        screen.blit(cursor, cursor_img_rect)
        pygame.display.flip()
