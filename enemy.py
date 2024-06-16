import pygame
import copy
import tank_shell


class EnemyTank:
    def __init__(self, screen, x, y):
        self.screen = screen
        self._pos = pygame.Vector2(x, y)
        self._hull_angle = 0
        self._turret_angle = 0
        self._speed = 300

        self.original_hull = pygame.image.load("assets/hull2.png").convert_alpha()
        self.original_hull = pygame.transform.rotate(self.original_hull, 180)
        width, height = self.original_hull.get_size()
        self.original_hull = pygame.transform.scale(self.original_hull, (width * 0.15, height * 0.15))

        self._rect = self.original_hull.get_rect()
        self._rect.center = self.pos

        self.original_turret = pygame.image.load("assets/turret.png").convert_alpha()
        width, height = self.original_turret.get_size()
        self.original_turret = pygame.transform.scale(self.original_turret, (width * 0.40, height * 0.40))

        self.hull = self.original_hull
        self.turret = self.original_turret

    def update(self, dt):
        self._rect.center = self.pos

    def shoot(self):
        return tank_shell.Shell(self.screen, copy.copy(self.pos), self.turret_angle - 90)

    def draw(self):
        # Rotate the hull
        rotated_hull = pygame.transform.rotate(self.original_hull, self.hull_angle)
        rotated_hull_rect = rotated_hull.get_rect(center=self.pos)

        # Rotate the turret
        rotated_turret = pygame.transform.rotate(self.original_turret, self.turret_angle - 90)
        rotated_turret_rect = rotated_turret.get_rect(center=self.pos)

        # Blit the rotated hull and turret to the screen
        self.screen.blit(rotated_hull, rotated_hull_rect)
        self.screen.blit(rotated_turret, rotated_turret_rect)

        self._rect.center = self.pos

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, value):
        self._rect = value

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value

    @property
    def hull_angle(self):
        return self._hull_angle

    @hull_angle.setter
    def hull_angle(self, value):
        self._hull_angle = value

    @property
    def turret_angle(self):
        return self._turret_angle

    @turret_angle.setter
    def turret_angle(self, value):
        self._turret_angle = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value
