import pygame


class Camera:
    def __init__(self, screen, map, player, entity_manager):
        self.screen = screen
        self.map = map

        self.map_surface = map.create_surface()
        self.map_rect = self.map_surface.get_rect(topleft=(0, 0))

        self.player = player
        self.entity_manager = entity_manager

        self.camera_rect = pygame.Rect(0, 0, self.screen.get_width(), self.screen.get_height())

        self.offset = pygame.Vector2(0, 0)
        self.half_w = self.screen.get_width() / 2
        self.half_h = self.screen.get_height() / 2

        # self.camera_rect = pygame.Rect(0, 0, self.screen.get_width(), self.screen.get_height())
        # self.camera_rect.center = self.player.pos

    def draw_2(self):
        self.centre_target_camera(self.player)

        map_offset = self.map_rect.topleft - self.offset
        self.screen.blit(self.map_surface, map_offset)

        self.player.draw()

        for enemy_tank in self.entity_manager.enemies:
            offset = enemy_tank.rect.topleft - self.offset
            self.screen.blit(enemy_tank.hull, offset)

        for bullet in self.entity_manager.bullets:
            offset = bullet.rect.topleft - self.offset
            self.screen.blit(bullet.image, offset)

        pygame.display.flip()

    def centre_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def apply(self, entity):
        return entity.rect.move(self.camera_rect.topleft)

    def update(self):
        x = -self.player.rect.x + self.half_w
        y = -self.player.rect.y + self.half_h

        self.camera_rect = pygame.Rect(x, y, self.camera_rect.width, self.camera_rect.height)

    def draw(self):
        self.centre_target_camera()
        self.screen.fill((0, 0, 0))

        for sprite in self.map.tile_sprites:
            self.screen.blit(sprite.image, self.apply(sprite))

        self.player.draw()

        for enemy_tank in self.entity_manager.enemies:
            self.screen.blit(enemy_tank.hull, self.apply(enemy_tank))

        for bullet in self.entity_manager.bullets:
            self.screen.blit(bullet.image, self.apply(bullet))

        pygame.display.flip()
