import pygame
import math


class Shell:
    def __init__(self, screen, pos, angle):
        self.screen = screen
        self.pos = pos
        self.angle = angle
        self.speed = 1000
        self.image = pygame.image.load("assets/tank_shell.png").convert_alpha()
        self.image = pygame.transform.rotate(self.image, 90)
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (width * 0.04, height * 0.04))

    def update(self, dt):
        self.pos.y -= self.speed * dt * math.cos(math.radians(self.angle))
        self.pos.x -= self.speed * dt * math.sin(math.radians(self.angle))

    def draw(self):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.pos)
        self.screen.blit(rotated_image, rotated_rect)
