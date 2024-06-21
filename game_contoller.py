import pygame
import tank
import tank_shell
import sys
import enemy
import random
import map
from entity_manager import EntityManager


class GameController:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
        self.running = True

        self.map = map.Map(self.screen, "maps/plains_map.tmx")

        self.fog_of_war = pygame.Surface((self.screen.get_width(), self.screen.get_height()))

        self.player = tank.Tank(self, self.screen, self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.entity_manager = EntityManager()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.entity_manager.bullets.append(self.player.shoot())

    def update(self, keys, mouse_pos, dt):
        if keys[pygame.K_g]:
            self.spawn_enemy()

        self.player.update(keys, mouse_pos, dt)
        self.update_bullets(dt)
        self.update_enemies(dt)

        self.check_collisions()

    def check_collisions(self):
        for bullet in self.entity_manager.bullets:
            for enemy_tank in self.entity_manager.enemies:
                if bullet.check_collision(enemy_tank):
                    self.entity_manager.bullets.remove(bullet)
                    self.entity_manager.enemies.remove(enemy_tank)
                    break

    def check_player_collision(self):
        for enemy_tank in self.entity_manager.enemies:
            if self.player.check_collision(enemy_tank):
                return True

    def update_bullets(self, dt):
        for bullet in self.entity_manager.bullets:
            bullet.update(dt)
            if not self.is_on_screen(bullet):
                self.entity_manager.bullets.remove(bullet)

    def update_enemies(self, dt):
        for enemy_tank in self.entity_manager.enemies:
            enemy_tank.update(dt)

    def spawn_enemy(self):
        new_enemy_pos = pygame.Vector2(random.randint(0, self.screen.get_width() - 50),
                                       random.randint(0, self.screen.get_height() - 50))
        self.entity_manager.create_enemy(self, self.screen, new_enemy_pos)

    def draw(self):
        # self.screen.fill((128, 0, 128))  # Purple background
        self.map.draw()
        # self.screen.blit(self.map, (0, 0))
        self.player.draw()

        for bullet in self.entity_manager.bullets:
            bullet.draw()

        for enemy_tank in self.entity_manager.enemies:
            enemy_tank.draw()

        pygame.display.flip()

    def is_on_screen(self, obj):
        return 0 <= obj.pos.x <= self.screen.get_width() and 0 <= obj.pos.y <= self.screen.get_height()

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000  # Delta time in seconds
            self.handle_events()

            keys = pygame.key.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            self.update(keys, mouse_pos, dt)

            self.draw()
        pygame.quit()
        sys.exit()
