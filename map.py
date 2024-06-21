import pygame
import pytmx
from pytmx.util_pygame import load_pygame


class Map:
    def __init__(self, screen, map_path):
        self.screen = screen
        self.map = load_pygame(map_path)
        self.tile_width = self.map.tilewidth
        self.tile_height = self.map.tileheight

    def draw(self):
        for layer in self.map.visible_layers:
            for x, y, gid in layer:
                tile = self.map.get_tile_image_by_gid(gid)
                if tile:
                    self.screen.blit(tile, (x * self.map.tilewidth, y * self.map.tileheight))

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
                if tile_properties and tile_properties.get('is_obstacle'):
                    return True
        return False

