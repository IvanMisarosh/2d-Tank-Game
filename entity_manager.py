import pygame
from enemy import EnemyTank
from tank_shell import Shell


class EntityManager:
    def __init__(self):
        self.bullets = []
        self.enemies = []
        self.obstacles = []

    def add_bullet(self, bullet):
        self.bullets.append(bullet)

    def create_enemy(self, game, screen, pos):
        self.enemies.append(EnemyTank(game, screen, pos))

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def remove_obstacle(self, obstacle):
        self.obstacles.remove(obstacle)

    @property
    def obstacles(self):
        return self._obstacles

    @obstacles.setter
    def obstacles(self, value):
        self._obstacles = value

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


