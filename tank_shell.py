import pygame
import math


class Shell:
    def __init__(self, screen, pos, angle, owner=None):
        self.owner = owner
        self.screen = screen
        self._pos = pos
        self._angle = angle
        self._speed = 1000
        self.image = pygame.image.load("assets/tank_shell.png").convert_alpha()
        self.image = pygame.transform.rotate(self.image, 90)
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (width * 0.04, height * 0.04))

        self._rect = self.image.get_rect()
        self._rect.center = self.pos

    def update(self, dt):
        self.pos.y -= self.speed * dt * math.cos(math.radians(self.angle))
        self.pos.x -= self.speed * dt * math.sin(math.radians(self.angle))

    def draw(self):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.pos)
        self.screen.blit(rotated_image, rotated_rect)

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
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value
