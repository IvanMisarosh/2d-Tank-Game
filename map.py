import pygame
import pytmx
from pytmx.util_pygame import load_pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)


class Map:
    def __init__(self, screen, map_path):
        self.screen = screen
        self.map = load_pygame(map_path)
        self.tile_width = self.map.tilewidth
        self.tile_height = self.map.tileheight
        self.tile_sprites = pygame.sprite.Group()

        self.create_tile_sprites()

    def create_tile_sprites(self):
        for layer in self.map.visible_layers:
            for x, y, gid in layer:
                tile = self.map.get_tile_image_by_gid(gid)
                if tile:
                    self.tile_sprites.add(Tile(tile, (x * self.map.tilewidth, y * self.map.tileheight)))

    def create_surface(self):
        # Create a surface with the same size as the map
        map_width = self.map.width * self.map.tilewidth
        map_height = self.map.height * self.map.tileheight
        surface = pygame.Surface((map_width, map_height))

        for layer in self.map.visible_layers:
            for x, y, gid in layer:
                tile = self.map.get_tile_image_by_gid(gid)
                if tile:
                    surface.blit(tile, (x * self.map.tilewidth, y * self.map.tileheight))

        return surface

    def get_tile_gid(self, x, y, layer_name):
        """Get the GID of the tile at the specified coordinates in the specified layer."""
        layer = self.map.get_layer_by_name(layer_name)
        if isinstance(layer, pytmx.TiledTileLayer):  # Ensure the layer is a tile layer
            return layer.data[y][x]  # Note: Tiled uses (y, x) indexing

    def get_tile_properties(self, x, y, layer_name):
        """Get the properties of the tile at the specified coordinates in the specified layer."""
        gid = self.get_tile_gid(x, y, layer_name)
        if gid:  # If a tile exists at this position
            return self.map.get_tile_properties_by_gid(gid)
        return None

    def is_obstacle(self, x, y):
        """Check if the tile at the specified coordinates has the 'obstacle' property set to True."""
        for layer in self.map.layers:
            if isinstance(layer, pytmx.TiledTileLayer):  # Ensure we only check tile layers
                tile_properties = self.get_tile_properties(x, y, layer.name)
                # if tile_properties and tile_properties.get('is_obstacle'):
                #     return True
        return False

