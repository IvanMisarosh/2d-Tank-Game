import pygame
import tank_shell
import math
import copy


class Tank:
    def __init__(self, game, screen, x, y):
        self.game = game
        self.screen = screen
        self._pos = pygame.Vector2(x, y)
        self._hull_angle = 0
        self._turret_angle = 0
        self._speed = 300

        self.original_hull = pygame.image.load("assets/hull2.png").convert_alpha()
        self.original_hull = pygame.transform.rotate(self.original_hull, 180)
        width, height = self.original_hull.get_size()
        self.original_hull = pygame.transform.scale(self.original_hull, (width * 0.12, height * 0.12))

        self._rect = self.original_hull.get_rect()
        self._mask = pygame.mask.from_surface(self.original_hull)

        self.original_turret = pygame.image.load("assets/turret.png").convert_alpha()
        width, height = self.original_turret.get_size()
        self.original_turret = pygame.transform.scale(self.original_turret, (width * 0.35, height * 0.35))
        self._turret_rect = self.original_turret.get_rect()

        self.hull = self.original_hull
        self.turret = self.original_turret
        self._rect.center = self.pos

    def update(self, keys, mouse_pos, offset, dt):
        # Adjust to compensate camera offset
        mouse_pos = mouse_pos + offset
        if keys:
            self.move(keys, dt)

        self.update_turret(mouse_pos)

    def update_turret(self, mouse_pos):

        self.turret_angle = math.degrees(math.atan2(-(mouse_pos[1] - self.pos.y), mouse_pos[0] - self.pos.x))
        # Rotate the turret
        self.turret = pygame.transform.rotate(self.original_turret, self.turret_angle - 90)
        self.turret_rect = self.turret.get_rect(center=self.pos)

    def check_collision(self, other):
        # return self.mask.overlap(other.mask, (int(other.pos.x - self.pos.x), int(other.pos.y - self.pos.y)))
        return pygame.sprite.collide_mask(self, other)

    def move(self, keys, dt):
        original_pos = self.pos.copy()  # Copy the original position to revert if collision occurs
        original_hull_angle = self.hull_angle

        if keys[pygame.K_w]:
            self.pos.y -= self.speed * dt * math.cos(math.radians(self.hull_angle))
            self.pos.x -= self.speed * dt * math.sin(math.radians(self.hull_angle))
        if keys[pygame.K_s]:
            self.pos.y += self.speed * dt * math.cos(math.radians(self.hull_angle))
            self.pos.x += self.speed * dt * math.sin(math.radians(self.hull_angle))
        if keys[pygame.K_a]:
            self.hull_angle += 100 * dt
        if keys[pygame.K_d]:
            self.hull_angle -= 100 * dt

        # TO DO: Remove code duplication
        self.hull = pygame.transform.rotate(self.original_hull, self.hull_angle)
        self._rect = self.hull.get_rect(center=self.pos)

        self._rect.center = self.pos
        self._mask = pygame.mask.from_surface(self.hull)

        if self.game.check_player_collision():
            self.pos = original_pos
            self.hull_angle = original_hull_angle
        else:
            self.hull = pygame.transform.rotate(self.original_hull, self.hull_angle)
            self._rect = self.hull.get_rect(center=self.pos)

            self._rect.center = self.pos
            self._mask = pygame.mask.from_surface(self.hull)

    def shoot(self):
        return tank_shell.Shell(self.screen, copy.copy(self.pos), self.turret_angle - 90, owner=self)

    def draw(self, offset):
        screen_hull_offset = self.rect.topleft - offset
        self.screen.blit(self.hull, screen_hull_offset)

        screen_turret_offset = self.turret_rect.topleft - offset
        self.screen.blit(self.turret, screen_turret_offset)

    @property
    def turret_rect(self):
        return self._turret_rect

    @turret_rect.setter
    def turret_rect(self, value):
        self._turret_rect = value

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

