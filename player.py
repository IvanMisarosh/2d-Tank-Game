from tank import Tank
import pygame
from health_bar import HealthBar


class Player(Tank):
    def __init__(self, game, screen, x, y, health=None):
        super().__init__(game, screen, x, y, health)
        self.health_bar = HealthBar(self.screen, self.health_percentage)

    def update(self, keys, mouse_pos, offset, dt):
        super().update(keys, mouse_pos, offset, dt)
        self.health_bar.health_percantage = self.health_percentage

    def draw(self, offset):
        super().draw(offset)
        self.health_bar.draw()
