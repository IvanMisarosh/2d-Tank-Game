import pygame
from core.single_player_game import SinglePlayerGame
from ui.main_menu import MainMenu


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

        # temporary solution for states
        self.states = []

        self.game = SinglePlayerGame()
        self.states.append(self.game)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in self.key_states:
                    self.key_states[event.key] = True
                if event.key == pygame.K_m:
                    self.states.append(MainMenu())
                elif event.key == pygame.K_ESCAPE:
                    if len(self.states) > 1:
                        self.states.pop()
            elif event.type == pygame.KEYUP:
                if event.key in self.key_states:
                    self.key_states[event.key] = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in self.key_states:
                    self.key_states[event.button] = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button in self.key_states:
                    self.key_states[event.button] = False

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000.0
            pygame.display.set_caption(f"My Game - FPS: {self.clock.get_fps():.0f}")

            self.handle_events()
            if isinstance(self.states[-1], SinglePlayerGame):
                self.states[-1].update(dt, self.key_states)
                self.states[-1].draw()
            else:
                self.game.draw()

                self.states[-1].update(dt, self.key_states)
                self.states[-1].draw()

            # Update the display
            pygame.display.flip()
