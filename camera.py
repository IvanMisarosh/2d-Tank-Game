import pygame


class Camera:
    def __init__(self, screen, map, player, entity_manager):
        self.screen = screen
        self.map = map

        self.player = player
        self.entity_manager = entity_manager

        self.offset = pygame.Vector2(0, 0)
        self.half_w = self.screen.get_width() / 2
        self.half_h = self.screen.get_height() / 2

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.centre_target_camera(self.player)

        # for floor_tile in self.entity_manager.floor_tiles:
        #     floor_tile.draw(self.offset)
        #
        # for obstacle in self.entity_manager.obstacles:
        #     obstacle.draw(self.offset)

        for i in range(self.map.map_size[0]):
            for j in range(self.map.map_size[1]):
                self.entity_manager.map_tiles[i][j].draw(self.offset)

        for enemy_tank in self.entity_manager.enemies:
            enemy_tank.draw(self.offset)

        for bullet in self.entity_manager.bullets:
            bullet.draw(self.offset)

        self.player.draw(self.offset)

        pygame.display.flip()

    def centre_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

