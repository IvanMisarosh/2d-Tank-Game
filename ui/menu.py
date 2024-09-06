import pygame
from ui.button import Button


class Menu:
    def __init__(self, screen,
                 x_screen_margin=75,
                 y_screen_margin=50,
                 button_cls=Button,
                 button_width=200,
                 button_height=50,
                 font=None,
                 button_margin=15,
                 menu_frame_width=2,
                 menu_frame_color=(255, 255, 255)):
        self.screen = screen
        self.x_screen_margin = x_screen_margin
        self.y_screen_margin = y_screen_margin
        self.button_cls = button_cls
        self.button_width = button_width
        self.button_height = button_height
        self.font = font or pygame.font.Font(None, 16)
        self.button_margin = button_margin
        self.menu_frame_width = menu_frame_width
        self.menu_frame_color = menu_frame_color

        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()

        self.buttons = []
        self.selected_button_index = None

        self.menu_surface = pygame.Surface((self.screen_width - 2 * self.x_screen_margin,
                                            self.screen_height - 2 * self.y_screen_margin),
                                           pygame.SRCALPHA)
        self.menu_surface.fill((0, 0, 0, 1))
        self.create_menu_frame()

    def update(self, key_states):
        if key_states[pygame.K_DOWN] or key_states[pygame.K_s]:
            self.select_next_button()
            key_states[pygame.K_DOWN] = False
            key_states[pygame.K_s] = False
        elif key_states[pygame.K_UP] or key_states[pygame.K_w]:
            self.select_previous_button()
            key_states[pygame.K_UP] = False
            key_states[pygame.K_w] = False
        elif key_states[pygame.K_RETURN]:
            self.buttons[self.selected_button_index].post_event()
            key_states[pygame.K_RETURN] = False

    def add_button(self, text, event_type):
        x = (self.menu_surface.get_width() - self.button_width) / 2
        y = len(self.buttons) * (self.button_height + self.button_margin) + self.button_margin
        button = self.button_cls(self.menu_surface,
                                 x,
                                 y,
                                 self.button_width,
                                 self.button_height,
                                 text,
                                 self.font,
                                 event_type)
        self.buttons.append(button)

    def select_next_button(self):
        if len(self.buttons) == 0:
            return

        if self.selected_button_index is None:
            self.selected_button_index = 0
            self.buttons[self.selected_button_index].make_selected()
        else:
            self.buttons[self.selected_button_index].make_unselected()
            self.selected_button_index = (self.selected_button_index + 1) % len(self.buttons)
            self.buttons[self.selected_button_index].make_selected()

    def select_previous_button(self):
        if len(self.buttons) == 0:
            return

        if self.selected_button_index is None:
            self.selected_button_index = 0
            self.buttons[self.selected_button_index].make_selected()
        else:
            self.buttons[self.selected_button_index].make_unselected()
            self.selected_button_index = (self.selected_button_index - 1) % len(self.buttons)
            self.buttons[self.selected_button_index].make_selected()

    def create_menu_frame(self):
        pygame.draw.rect(self.menu_surface, self.menu_frame_color, (0,
                                                                    0,
                                                                    self.menu_surface.get_width(),
                                                                    self.menu_frame_width))
        pygame.draw.rect(self.menu_surface, self.menu_frame_color, (0,
                                                                    0,
                                                                    self.menu_frame_width,
                                                                    self.menu_surface.get_height()))
        pygame.draw.rect(self.menu_surface, self.menu_frame_color, (0,
                                                                    self.menu_surface.get_height() - self.menu_frame_width,
                                                                    self.menu_surface.get_width(),
                                                                    self.menu_frame_width))
        pygame.draw.rect(self.menu_surface, self.menu_frame_color, (self.menu_surface.get_width() - self.menu_frame_width,
                                                                    0,
                                                                    self.menu_frame_width,
                                                                    self.menu_surface.get_height()))

    def create_escape_label(self):
        font = pygame.font.Font(None, 32)
        escape_label = font.render("Press ESC to return", True, (255, 255, 255))
        escape_label_rect = escape_label.get_rect(center=(150,
                                                          30))
        self.menu_surface.blit(escape_label, escape_label_rect)

    def draw(self):
        self.menu_surface.fill((0, 0, 0, 0))  # transparent background

        self.create_menu_frame()
        self.create_escape_label()

        for button in self.buttons:
            button.draw()

        self.screen.blit(self.menu_surface, (self.x_screen_margin, self.y_screen_margin))

