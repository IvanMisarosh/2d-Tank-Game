import pygame
import math


class Tank:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.pos = pygame.Vector2(x, y)
        self.hull_angle = 0
        self.turret_angle = 0
        self.speed = 300

        self.original_hull = pygame.image.load("assets/hull2.png").convert_alpha()
        self.original_hull = pygame.transform.rotate(self.original_hull, 180)
        width, height = self.original_hull.get_size()
        self.original_hull = pygame.transform.scale(self.original_hull, (width * 0.15, height * 0.15))

        self.original_turret = pygame.image.load("assets/turret.png").convert_alpha()
        width, height = self.original_turret.get_size()
        self.original_turret = pygame.transform.scale(self.original_turret, (width * 0.40, height * 0.40))

        self.hull = self.original_hull
        self.turret = self.original_turret

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos.y -= self.speed * dt * math.cos(math.radians(self.hull_angle))
            self.pos.x -= self.speed * dt * math.sin(math.radians(self.hull_angle))
        if keys[pygame.K_s]:
            self.pos.y += self.speed * dt * math.cos(math.radians(self.hull_angle))
            self.pos.x += self.speed * dt * math.sin(math.radians(self.hull_angle))
        if keys[pygame.K_a]:
            self.hull_angle += 100 * dt
        if keys[pygame.K_d]:
            self.hull_angle += -100 * dt

        mouse_pos = pygame.mouse.get_pos()
        self.turret_angle = math.degrees(math.atan2(-(mouse_pos[1] - self.pos.y), mouse_pos[0] - self.pos.x))

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



