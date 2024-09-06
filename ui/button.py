import pygame


class Button:
    # TODO: Add hover effect
    # TODO: Ensure font is initialized
    def __init__(self, screen,
                 x,
                 y,
                 width,
                 height,
                 text,
                 font,
                 event_type,
                 border_width=2,
                 border_color=(0, 0, 0),
                 bg_color=(255, 255, 255),
                 selected_color=(0, 0, 255)):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.event_type = event_type
        self.border_width = border_width
        self.border_color = border_color
        self.bg_color = bg_color
        self.selected_color = selected_color

        self.is_selected = False
        self.current_color = self.bg_color

    def post_event(self):
        custom_event = pygame.event.Event(self.event_type)
        pygame.event.post(custom_event)

    def make_selected(self):
        self.current_color = self.selected_color
        self.is_selected = True

    def make_unselected(self):
        self.current_color = self.bg_color
        self.is_selected = False

    def draw(self):

        pygame.draw.rect(self.screen, self.border_color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.screen, self.current_color, (self.x + self.border_width, self.y + self.border_width, self.width - 2 * self.border_width, self.height - 2 * self.border_width))

        text = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        self.screen.blit(text, text_rect)
