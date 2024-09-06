import pygame
from core.game_state import GameState
from ui.menu import Menu


class SettingsMenu(GameState):
    def __init__(self):
        self.screen = pygame.display.get_surface()

        self.canvas = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        self.canvas.fill((0, 0, 0, 128))

        # self.menu = Menu(self.canvas)
        # self.setup_menu()

    def setup_menu(self):
        pass

    def set_caption(self):
        font = pygame.font.Font(None, 52)
        escape_label = font.render("NOTHING TO SEE HERE YET", True, (255, 255, 255))
        escape_label_rect = escape_label.get_rect(center=(self.screen.get_width() / 2,
                                                          self.screen.get_height() / 2))
        self.canvas.blit(escape_label, escape_label_rect)

    def update(self, dt, key_states):
        pass

    def draw(self):
        self.set_caption()
        self.screen.blit(self.canvas, (0, 0))

        # self.menu.draw()

        pygame.display.flip()
