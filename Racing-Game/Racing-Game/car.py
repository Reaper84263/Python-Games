import random
from vehicle import Vehicle

class Car(Vehicle):
    """Car with nitro special."""

    def __init__(self, name="Lightning Car", speed=7):
        super().__init__(name, "C", speed)

    def special_move(self, obs, *, finish):
        if self.energy >= 15:
            self.energy -= 15
            base = int(self._speed * 1.5)
            move = random.randint(max(0, base - 1), base + 1)
            d = self._distance_to_obstacle(obs)
            if d is not None and move >= d:
                self.position = min(self.position + d, finish)
                return f"{self._name} uses nitro boost but CRASHED into an obstacle!"
            self.position = min(self.position + move, finish)
            return f"{self._name} uses nitro boost and moves {move} units!"
        before = self.position
        self.position = min(self.position + 1, finish)
        return f"{self._name} tries to use nitro, but is all out of energy!"
