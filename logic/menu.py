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


class Settings:
    def __init__(self, screen):
        self.screen = screen

        self.font = pygame.font.Font(logic.constants.FONT_PATH, 75)
        self.manager = TextInputManager(
            validator=lambda input: (input.isnumeric() and 0 < int(input) <= logic.constants.WIDTH) or input == '',
            initial=str(logic.constants.WIDTH))
        self.textinput = TextInputVisualizer(manager=self.manager, font_object=self.font)
        self.textinput.cursor_width = 4
        self.textinput.cursor_blink_interval = 400
        self.textinput.antialias = False
        self.textinput.font_color = 'blue'
        self.textinput.cursor_color = 'blue'
        self.manager2 = TextInputManager(
            validator=lambda input: (input.isnumeric() and 0 < int(input) <= logic.constants.HEIGHT) or input == '',
            initial=str(logic.constants.HEIGHT))
        self.textinput2 = TextInputVisualizer(manager=self.manager2, font_object=self.font)
        self.textinput2.cursor_width = 4
        self.textinput2.cursor_blink_interval = 400
        self.textinput2.antialias = False
        self.textinput2.font_color = 'blue'
        self.textinput2.cursor_color = 'blue'

        pygame.key.set_repeat(200, 25)
        self.set_fon = Settings_fon(self.screen,
                                    (105, 105), (logic.constants.WIDTH - 210, logic.constants.HEIGHT - 210), 'white')
        self.settings_texts = [Text('Настройки', 75, (logic.constants.WIDTH // 2, self.set_fon.rect.y + 50), 'black'),
                               Text('Размеры Окна', 60, (self.set_fon.rect.x + 200, self.set_fon.rect.y + 150), 'black')



                               ]

    def draw(self):

        self.set_fon.draw()

        for text in self.settings_texts:
            self.screen.blit(text.text, text.rect)
        cross_text = self.font.render('x', True, 'blue')




        # self.screen.blit(self.textinput.surface, (self.set_fon.width // 1.5, main_text_rect.y + 100))
        # self.screen.blit(self.textinput2.surface, (set_fon.width // 1.5 + 260, main_text_rect.y + 100))
        # self.inp_rect_1 = Rect((set_fon.width // 1.5 - 10, main_text_rect.y + 100 - 5,
        #                         self.textinput.surface.get_rect().width - 20,
        #                         self.textinput.surface.get_rect().height + 5))
        # self.inp_rect_2 = Rect((set_fon.width // 1.5 + 250, main_text_rect.y + 100 - 5,
        #                         self.textinput2.surface.get_rect().width - 20,
        #                         self.textinput2.surface.get_rect().height + 5))
        # cross_text_rect = cross_text.get_rect(
        #     center=(self.inp_rect_1.x + self.inp_rect_1.width + (
        #             self.inp_rect_2.x - (self.inp_rect_1.x + self.inp_rect_1.width)) // 2,
        #             self.inp_rect_1.y + self.inp_rect_1.height // 2))
        # self.screen.blit(cross_text, cross_text_rect)
        # pygame.draw.rect(self.screen, 'red', self.inp_rect_1
        #                  ,
        #                  5)
        # pygame.draw.rect(self.screen, 'red', self.inp_rect_2
        #                  ,
        #                  5)


# Код Рената --------------------------------------
def load_menu(screen, clock):
    btn_colors = [0, 0, 0]
    settings = Settings(screen)
    settings.draw()
    colors = logic.constants.BTN_COLOR
    center_pos = logic.constants.WIDTH // 2
    start_btn = Buttons('Начать', colors[btn_colors[0]], (center_pos, logic.constants.HEIGHT // 2))
    resume_btn = Buttons('Продолжить', colors[btn_colors[1]],
                         (center_pos, logic.constants.HEIGHT // 2 + start_btn.rect.height * 2))
    settings_btn = Buttons('Настройки', colors[btn_colors[2]],
                           (center_pos, logic.constants.HEIGHT // 2 + resume_btn.rect.height * 4))
    buttons = [start_btn, resume_btn, settings_btn]
    #input_fields = [settings.inp_rect_1, settings.inp_rect_2]
    is_opened_set = False
    active_input_field = 0
    for button in buttons:
        screen.blit(button.text, (button.pos_x, button.pos_y))

    while True:
        screen.fill('white')
        # fon = pygame.transform.scale(load_image(logic.constants.MENU_FON_PATH), (logic.constants.SIZE))

        # screen.blit(fon, (0, 0))
        events = pygame.event.get()

        if active_input_field == 0:

            settings.textinput.update(events)



        elif active_input_field == 1:

            settings.textinput2.update(events)

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

            # for i, field in enumerate(input_fields):
            #     if field.collidepoint(pygame.mouse.get_pos()):
            #
            #         if pygame.mouse.get_pressed()[0] and i == 0:
            #             active_input_field = 0
            #             init((int(settings.textinput.value), int(settings.textinput2.value)))
            #             load_menu(screen, clock)
            #         elif pygame.mouse.get_pressed()[0] and i == 1:
            #             active_input_field = 1

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
        pygame.display.flip()
