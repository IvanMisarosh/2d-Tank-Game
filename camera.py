import pygame


class Camera:
    def __init__(self, screen, map, player):
        self.screen = screen
        self.map = map
        self.player = player