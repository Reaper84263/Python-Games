import random
from vehicle import Vehicle

class Motorcycle(Vehicle):
    """Motorcycle with wheelie special."""

    def __init__(self, name="Swift Bike", speed=8):
        super().__init__(name, "M", speed)

    def slow(self, obs, *, finish):
        base = int(round(self._speed * 0.75))
        move = random.randint(max(0, base - 1), base + 1)
        d = self._distance_to_obstacle(obs)
        before = self.position
        if d is not None and move >= d:
            self.position = min(obs + 1, finish)
            return f"{self._name} slowly dodges the obstacle and moves {self.position - before} units!"
        self.position = min(self.position + move, finish)
        return f"{self._name} slowly moves {move} units!"

    def special_move(self, obs, *, finish):
        if self.energy >= 15:
            self.energy -= 15
            if random.randint(1, 100) <= 75:
                base = self._speed * 2
                move = random.randint(max(0, base - 1), base + 1)
                d = self._distance_to_obstacle(obs)
                if d is not None and move >= d:
                    self.position = min(self.position + d, finish)
                    return f"{self._name} pops a wheelie but CRASHED into an obstacle!"
                self.position = min(self.position + move, finish)
                return f"{self._name} pops a wheelie and moves {move} units!!"
            before = self.position
            self.position = min(self.position + 1, finish)
            return f"{self._name} tries a wheelie but wipes out and moves {self.position - before} unit!"
        before = self.position
        self.position = min(self.position + 1, finish)
        return f"{self._name} tries a wheelie, but is all out of energy!"

