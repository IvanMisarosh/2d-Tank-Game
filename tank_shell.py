import pygame
import math


class Shell:
    def __init__(self, screen, pos, angle, owner=None):
        self.owner = owner
        self.screen = screen
        self._pos = pos
        self._angle = angle
        self._speed = 1000
        self.original_image = pygame.image.load("assets/tank_shell.png").convert_alpha()
        width, height = self.original_image.get_size()
        self.original_image = pygame.transform.scale(self.original_image, (width * 0.04, height * 0.04))
        self.image = self.original_image

        self._rect = self.image.get_rect()
        self._rect.center = self.pos
        self._mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        self.pos.y -= self.speed * dt * math.cos(math.radians(self.angle))
        self.pos.x -= self.speed * dt * math.sin(math.radians(self.angle))

        self.image = pygame.transform.rotate(self.original_image, self.angle + 90)
        self._rect = self.image.get_rect(center=self.pos)
        self._mask = pygame.mask.from_surface(self.image)

    def draw(self, offset):
        # self.screen.blit(self.image, self._rect)
        screen_offset = self.rect.topleft - offset
        self.screen.blit(self.image, screen_offset)

    def check_collision(self, other):
        if self.rect.colliderect(other.rect):
            return pygame.sprite.collide_mask(self, other)

    @property
    def mask(self):
        return self._mask

    @mask.setter
    def mask(self, value):
        self._mask = value

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
