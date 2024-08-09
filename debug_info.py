from tank import Tank
import pygame


class DebugInfo:
    def __init__(self, player: Tank):
        self.player = player
        self.font = pygame.font.Font('freesansbold.ttf', 16)

    def draw(self):
        text = (f"Player info:\n  Speed: {self.player.speed}\n  Position: {self.player.rect.topleft}\n  "
                f"Hull angle: {round(self.player.hull_angle, 1)}\n  Turret angle: {round(self.player.turret_angle, 1)}\n  "
                f"Max health: {self.player.max_health}\n  Current health: {self.player.health}\n  "
                f"Health percentage: {self.player.health_percentage}")

        self.box_text(self.player.screen, self.player.screen.get_width() - 210
                      , self.player.screen.get_width() - 20
                      , 10, text, (255, 0, 0))

    def box_text(self, surface, x_start, x_end, y_start, text, colour):
        x = x_start
        y = y_start
        words = text.split('\n')

        for word in words:
            word_t = self.font.render(word, True, colour)
            if word_t.get_width() + x <= x_end:
                surface.blit(word_t, (x, y))
                x += word_t.get_width() * 1.1
            else:
                y += word_t.get_height() * 1.1
                x = x_start
                surface.blit(word_t, (x, y))
                x += word_t.get_width() * 1.1
