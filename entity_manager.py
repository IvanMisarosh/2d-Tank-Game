from enemy import EnemyTank
from settings import *


class EntityManager:
    def __init__(self):
        self._bullets = []
        self._enemies = []
        self.map_tiles = None

    def add_bullet(self, bullet):
        self.bullets.append(bullet)

    def create_enemy(self, game, screen, pos):
        self.enemies.append(EnemyTank(game, screen, pos))

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)

    def get_surronding_tiles(self, pos):
        x, y = pos
        x = int(x // TILE_SIZE)
        y = int(y // TILE_SIZE)
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # Top-left, Top, Top-right
            (0, -1),           (0, 1),  # Left,       , Right
            (1, -1),  (1, 0),  (1, 1)  # Bottom-left, Bottom, Bottom-right
        ]

        surrounding_elements = []
        try:
            surrounding_elements.append(self.map_tiles[x][y])
        except IndexError:
            pass

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self.map_tiles) and 0 <= ny < len(self.map_tiles[0]):
                surrounding_elements.append(self.map_tiles[nx][ny])

        return surrounding_elements

    @property
    def bullets(self):
        return self._bullets

    @bullets.setter
    def bullets(self, value):
        self._bullets = value

    @property
    def enemies(self):
        return self._enemies

    @enemies.setter
    def enemies(self, value):
        self._enemies = value
