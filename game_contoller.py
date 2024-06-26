import pygame
import tank
import tank_shell
import sys
import enemy
import random
import map
from entity_manager import EntityManager
from camera import Camera


class GameController:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
        self.running = True

        self.entity_manager = EntityManager()

        self.map = map.GridMap(self.entity_manager, "maps/30_30_test_map.txt")

        self.player = tank.Tank(self, self.screen, self.screen.get_width() / 2, self.screen.get_height() / 2)

        self.camera = Camera(self.screen, self.map, self.player, self.entity_manager)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.entity_manager.add_bullet(self.player.shoot())

    def update(self, keys, mouse_pos, dt):

        self.camera.centre_target_camera(self.player)
        if keys[pygame.K_g]:
            self.spawn_enemy()

        self.player.update(keys, mouse_pos, self.camera.offset, dt)
        pygame.display.set_caption(f"My Game - FPS: {self.clock.get_fps()}")
        self.update_bullets(dt)
        self.update_enemies(dt)

        self.check_collisions()

    def check_collisions(self):
        for bullet in self.entity_manager.bullets:
            res = self.check_enemy_collision(bullet)
            if res:
                self.entity_manager.remove_bullet(bullet)
                self.entity_manager.remove_enemy(res[1])

            res = self.check_wall_collisions(bullet)
            if res:
                self.entity_manager.remove_bullet(bullet)
                self.entity_manager.remove_obstacle(res[1])

    def check_player_collision(self):
        if self.check_enemy_collision(self.player) or self.check_wall_collisions(self.player):
            return True

    def check_enemy_collision(self, entity):
        for enemy_tank in self.entity_manager.enemies:
            if entity.check_collision(enemy_tank):
                return True, enemy_tank

    def check_wall_collisions(self, entity):
        for obstacle in self.entity_manager.obstacles:
            if entity.check_collision(obstacle):
                return True, obstacle

    def update_bullets(self, dt):
        for bullet in self.entity_manager.bullets:
            bullet.update(dt)
            if not self.is_on_screen(bullet):
                self.entity_manager.remove_bullet(bullet)

    def update_enemies(self, dt):
        for enemy_tank in self.entity_manager.enemies:
            enemy_tank.update(dt)

    def spawn_enemy(self):
        new_enemy_pos = pygame.Vector2(random.randint(0, self.screen.get_width() - 50),
                                       random.randint(0, self.screen.get_height() - 50))
        self.entity_manager.create_enemy(self, self.screen, new_enemy_pos)

    def draw(self):
        self.camera.draw()

    def is_on_screen(self, obj):
        # Adjust camera offset
        screen_pos = obj.rect.topleft - self.camera.offset

        return 0 <= screen_pos[0] <= self.screen.get_width() and 0 <= screen_pos[1] <= self.screen.get_height()

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
