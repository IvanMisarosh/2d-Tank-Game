import pygame


class Camera:
    def __init__(self, screen, map, player, entity_manager):
        self.screen = screen
        self.map = map

        self.map_surface = map.create_surface()
        self.map_rect = self.map_surface.get_rect(topleft=(0, 0))

        self.player = player
        self.entity_manager = entity_manager

        self.offset = pygame.Vector2(0, 0)
        self.half_w = self.screen.get_width() / 2
        self.half_h = self.screen.get_height() / 2

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.centre_target_camera(self.player)

        map_offset = self.map_rect.topleft - self.offset
        self.screen.blit(self.map_surface, map_offset)

        # player_offset = self.player.rect.topleft - self.offset
        self.player.draw(self.offset)
        # self.screen.blit(self.player.hull, player_offset)

        for enemy_tank in self.entity_manager.enemies:
            # offset = enemy_tank.rect.topleft - self.offset
            # self.screen.blit(enemy_tank.hull, offset)
            enemy_tank.draw(self.offset)
        for bullet in self.entity_manager.bullets:
            # offset = bullet.rect.topleft - self.offset
            # self.screen.blit(bullet.image, offset)
            bullet.draw(self.offset)

        pygame.display.flip()

    def centre_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h
