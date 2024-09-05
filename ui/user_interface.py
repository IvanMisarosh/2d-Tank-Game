from ui.health_bar import HealthBar
from ui.debug_info import DebugInfo


class UserInterface:
    def __init__(self, player, debug=False):
        self.player = player
        self.health_bar = HealthBar(self.player)
        self.debug_info = DebugInfo(self.player) if debug else None

    def update(self):
        # self.health_bar.update()
        pass

    def draw(self):
        self.health_bar.draw()
        if self.debug_info:
            self.debug_info.draw()
