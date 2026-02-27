import random
from vehicle import Vehicle

class Truck(Vehicle):
    """Truck that rams through obstacles."""

    def __init__(self, name="Behemoth Truck", speed=6):
        super().__init__(name, "T", speed)

    def special_move(self, obs, *, finish):
        if self.energy >= 15:
            self.energy -= 15
            base = self._speed * 2
            move = random.randint(max(0, base - 1), base + 1)
            before = self.position
            self.position = min(self.position + move, finish)
            return f"{self._name} rams forward {self.position - before} units!"
        return f"{self._name} tries to ram forward, but is all out of energy!"

