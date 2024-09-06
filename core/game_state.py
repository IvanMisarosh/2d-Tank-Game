from abc import ABC, abstractmethod


class GameState(ABC):
    @abstractmethod
    def update(self, dt, key_states):
        pass

    @abstractmethod
    def draw(self):
        pass
