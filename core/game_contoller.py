import pygame
from core.single_player_game import SinglePlayerGame


class GameController:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.states = []
        self.states.append(SinglePlayerGame())

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000.0
            pygame.display.set_caption(f"My Game - FPS: {self.clock.get_fps()}")

            self.handle_events()
            self.states[-1].update(dt)
            self.states[-1].draw()
