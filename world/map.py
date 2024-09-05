import pygame
from abc import ABC, abstractmethod
from core.settings import *
import random

color_codes = {
    "0": BLACK,
    "1": ORANGE,
    "2": BLUE
}


class Tile(ABC):
    texture = pygame.image.load("assets/default_texture.png")

    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = self.texture
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, offset):
        screen_offset = self.rect.topleft - offset
        self.screen.blit(self.image, screen_offset)

    @property
    @abstractmethod
    def is_obstacle(self):
        pass


class Wall(Tile):
    texture = pygame.image.load("assets/wall.png")

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)

    @property
    def is_obstacle(self):
        return True


class Floor(Tile):
    texture = pygame.image.load("assets/floor.png")

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)

    @property
    def is_obstacle(self):
        return False


class GridMap:
    def __init__(self, entity_manager, map_path=None):
        self.screen = pygame.display.get_surface()
        self.entity_manager = entity_manager
        self.map_path = map_path
        self.map_size = None
        self.tile_size = TILE_SIZE

        self.load_map()

    def load_map(self):
        map_tiles = []
        if self.map_path:
            with open(self.map_path, "r") as file:
                lines = file.readlines()
                # self.map_size = map(int, lines[0].strip().split(","))
                self.map_size = [int(x) for x in lines[0].strip().split(",")]
                print(self.map_size)
                for i, line in enumerate(lines[1:]):
                    row = []
                    for j, code in enumerate(line.strip().split()):
                        tile = None
                        color = None
                        if code in color_codes:
                            color = color_codes[code]
                        if color is None:
                            # TODO: Handle error
                            return
                        if color == ORANGE:
                            tile = Wall(self.screen, i * self.tile_size, j * self.tile_size)
                        elif color == BLACK:
                            tile = Floor(self.screen, i * self.tile_size, j * self.tile_size)
                        elif color == BLUE:
                            # TODO: Add spawn point tiles
                            # self.entity_manager.add_spawn_point(j * self.tile_size, i * self.tile_size)
                            pass
                        row.append(tile)
                    map_tiles.append(row)
        self.entity_manager.map_tiles = map_tiles

    def draw_grid(self, surface):
        for x in range(0, self.map_size[0], self.tile_size):
            for y in range(0, self.map_size[1], self.tile_size):
                self.entity_manager.add_floor_tile(Floor(self.screen, x, y))

    def create_obstacles(self):
        for x in range(0, self.map_size[0], self.tile_size):
            for y in range(0, self.map_size[1], self.tile_size):
                if random.randint(0, 100) < 20:
                    self.entity_manager.add_obstacle(Wall(self.screen, x, y))

    def create_surface(self):
        surface = pygame.Surface(self.map_size)
        # self.draw_grid(surface)
        # self.draw_grid(surface)
        # self.create_obstacles()  # Use self.game, no need to pass surface
        return surface

