import pygame


class Tank:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.pos = pygame.Vector2(x, y)
        self.speed = 300

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos.y -= self.speed * dt
        if keys[pygame.K_s]:
            self.pos.y += self.speed * dt
        if keys[pygame.K_a]:
            self.pos.x -= self.speed * dt
        if keys[pygame.K_d]:
            self.pos.x += self.speed * dt

    def draw(self):
        pygame.draw.rect(self.screen, "red", (self.pos.x - 20, self.pos.y - 20, 40, 40))
        pygame.draw.rect(self.screen, "black", (self.pos.x - 5, self.pos.y - 40, 10, 40))