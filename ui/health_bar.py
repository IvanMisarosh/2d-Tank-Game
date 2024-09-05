import pygame
from entities.tank import Tank


class HealthBar:
    def __init__(self, player: Tank):
        self.player = player
        self.screen = player.screen
        self.margin_right = 20
        self.margin_bottom = 50
        self.rect_width = 154
        self.rect_height = 34

    def draw(self):
        x = self.screen.get_width() - self.rect_width - self.margin_right
        y = self.screen.get_height() - self.margin_bottom

        # base rect for black border
        pygame.draw.rect(self.screen, (0, 0, 0), (x
                                                  , y
                                                  , self.rect_width
                                                  , self.rect_height))

        # grey rect for background
        pygame.draw.rect(self.screen, (150, 150, 150), (x + 2
                                                        , y + 2
                                                        , self.rect_width - 4
                                                        , self.rect_height - 4))

        # red rect for health
        # # for test purposes
        # self.health = self.get_random_health()
        pygame.draw.rect(self.screen, (255, 0, 0), (x + 2
                                                    , y + 2
                                                    , int((self.rect_width - 4) * self.health_percentage)
                                                    , self.rect_height - 4))

    @property
    def health_percentage(self):
        return self.player.health_percentage
