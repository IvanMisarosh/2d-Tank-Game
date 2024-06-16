import pygame
import math


class Tank:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.pos = pygame.Vector2(x, y)
        self.hull_angle = 0
        self.turret_angle = 0
        self.speed = 300

        self.original_hull = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.original_turret = pygame.Surface((10, 50), pygame.SRCALPHA)
        self.original_hull.fill((255, 0, 0))  # Red rectangle
        self.original_turret.fill((0, 255, 0))  # Green rectangle

        self.hull = self.original_hull
        self.turret = self.original_turret


    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos.y -= self.speed * dt * math.cos(math.radians(self.hull_angle))
            self.pos.x -= self.speed * dt * math.sin(math.radians(self.hull_angle))
        if keys[pygame.K_s]:
            self.pos.y += self.speed * dt
        if keys[pygame.K_a]:
            self.hull_angle += 100 * dt
        if keys[pygame.K_d]:
            self.hull_angle += -100 * dt
        if pygame.mouse.get_rel()[0] > 0 or pygame.mouse.get_rel()[1] > 0:
            mouse_pos = pygame.mouse.get_pos()

    def draw(self):
        player_image = pygame.Surface((100, 100), pygame.SRCALPHA)
        player_image.blit(self.hull, (5, 20))  # Position rect1 within the player image
        player_image.blit(self.turret, (25, 0))  # Position rect2 within the player image

        player_image = pygame.transform.rotate(player_image, self.hull_angle)
        player_rect = player_image.get_rect(center=self.pos)

        self.screen.blit(player_image, player_rect)

