import pygame
import core.custom_events as custom_events
from core.single_player_game import SinglePlayerGame
from ui.main_menu import MainMenu
from ui.settings_menu import SettingsMenu


class GameController:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True

        self.key_states = {
            pygame.K_DOWN: False,
            pygame.K_s: False,
            pygame.K_UP: False,
            pygame.K_w: False,
            pygame.K_RETURN: False,
            pygame.K_g: False,
            pygame.BUTTON_LEFT: False,
        }

        # temporary? solution for states
        # TODO: implement a proper state machine
        self.overlay_states = []
        self.overlay_states_lookup = dict()

        self.game_state = None

        self.append_game_state(MainMenu)

    def append_game_state(self, game_state_cls, *args, **kwargs):
        print(game_state_cls.__name__)
        if not self.overlay_states_lookup.get(game_state_cls.__name__):
            self.overlay_states_lookup[game_state_cls.__name__] = True
            self.overlay_states.append(game_state_cls(*args, **kwargs))

    def pop_game_state(self):
        if not self.overlay_states:
            return
        state = self.overlay_states.pop()
        self.overlay_states_lookup[state.__class__.__name__] = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in self.key_states:
                    self.key_states[event.key] = True
                elif event.key == pygame.K_ESCAPE:
                    if len(self.overlay_states) > 1:
                        self.pop_game_state()
                    elif len(self.overlay_states) == 0 and self.game_state:
                        self.append_game_state(MainMenu)
            elif event.type == pygame.KEYUP:
                if event.key in self.key_states:
                    self.key_states[event.key] = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in self.key_states:
                    self.key_states[event.button] = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button in self.key_states:
                    self.key_states[event.button] = False
            elif event.type == custom_events.START_SINGLE_PLAYER_GAME:
                if not self.game_state:
                    self.pop_game_state()
                    self.game_state = SinglePlayerGame()
            elif event.type == custom_events.START_MULTI_PLAYER_GAME:
                pass
            elif event.type == custom_events.OPEN_SETTINGS_MENU:
                self.append_game_state(SettingsMenu)

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000.0
            pygame.display.set_caption(f"My Game - FPS: {self.clock.get_fps():.0f}")

            self.handle_events()
            if self.game_state:
                self.game_state.update(dt, self.key_states)
                self.game_state.draw()

            if self.overlay_states:
                self.overlay_states[-1].update(dt, self.key_states)
                self.overlay_states[-1].draw()

            # Update the display
            pygame.display.flip()
