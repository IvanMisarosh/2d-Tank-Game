import pygame
from health_bar import HealthBar


class UserInterface:
    def __init__(self, player):
        self.player = player
        self.health_bar = HealthBar(self.player)

    def update(self):
        # self.health_bar.update()
        pass

    def draw(self):
        self.health_bar.draw()
