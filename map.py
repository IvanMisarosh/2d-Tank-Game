import pygame
import pytmx
from pytmx.util_pygame import load_pygame
from abc import ABC, abstractmethod
from settings import *
import random


class AbstractMap(ABC):
    @abstractmethod
    def create_surface(self):
        pass


class Wall:
    def __init__(self, screen, x, y, width=TILE_SIZE, height=TILE_SIZE):
        self.screen = screen
        self.image = pygame.Surface((width, height))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, offset):
        screen_offset = self.rect.topleft - offset
        self.screen.blit(self.image, screen_offset)


class GridMap(AbstractMap):
    def __init__(self, screen, entity_maneger, map_size, tile_size):
        self.screen = screen
        self.entity_maneger = entity_maneger
        self.map_size = map_size
        self.tile_size = tile_size
        self.tiles = []

    def draw_grid(self, surface):
        for x in range(0, self.map_size[0], self.tile_size):
            pygame.draw.line(surface, LIGHT_GREY, (x, 0), (x, self.map_size[1]))

        for y in range(0, self.map_size[1], self.tile_size):
            pygame.draw.line(surface, LIGHT_GREY, (0, y), (self.map_size[0], y))

    def create_obstacles(self):
        for x in range(0, self.map_size[0], self.tile_size):
            for y in range(0, self.map_size[1], self.tile_size):
                if random.randint(0, 100) < 20:
                    self.entity_maneger.add_obstacle(Wall(self.screen, x, y))

    def create_surface(self):
        surface = pygame.Surface(self.map_size)
        self.draw_grid(surface)
        self.create_obstacles()  # Use self.game, no need to pass surface
        return surface

