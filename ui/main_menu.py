from core.game_state import GameState
from ui.menu import Menu
import core.custom_events as custom_events
import pygame


class MainMenu(GameState):
    def __init__(self):
        self.screen = pygame.display.get_surface()

        self.canvas = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        self.canvas.fill((0, 0, 0, 128))

        self.menu = Menu(self.canvas)
        self.setup_menu()

    def setup_menu(self):
        self.menu.add_button("Single Player", custom_events.START_SINGLE_PLAYER_GAME)
        self.menu.add_button("Multi Player", custom_events.START_MULTI_PLAYER_GAME)
        self.menu.add_button("Settings", custom_events.OPEN_SETTINGS_MENU)
        self.menu.add_button("Quit", pygame.QUIT)

    def update(self, dt, key_states):
        self.menu.update(key_states)

    def draw(self):

        self.screen.blit(self.canvas, (0, 0))
        self.menu.draw()

        pygame.display.flip()
