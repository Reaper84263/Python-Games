import random
from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Abstract racing vehicle."""

    def __init__(self, name, initial, speed):
        self._name = name
        self._initial = initial
        self._speed = speed
        self._position = 0
        self._energy = 100

    @property
    def initial(self):
        return self._initial

    @initial.setter
    def initial(self, v):
        self._initial = v

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, v):
        self._position = v

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, v):
        self._energy = max(0, min(100, v))

    def _distance_to_obstacle(self, obs):
        if obs is None or obs <= self._position:
            return None
        return obs - self._position

    def _cap(self, pos, finish):
        return min(pos, finish)

    def fast(self, obs, *, finish):
        if self._energy >= 5:
            move = random.randint(max(0, self._speed - 1), self._speed + 1)
            self._energy -= 5
            d = self._distance_to_obstacle(obs)
            if d is not None and move >= d:
                self._position = self._cap(self._position + d, finish)
                return f"{self._name} CRASHED into an obstacle!"
            self._position = self._cap(self._position + move, finish)
            return f"{self._name} quickly moves {move} units!"
        before = self._position
        self._position = self._cap(self._position + 1, finish)
        return f"{self._name} is tired but still moves {self._position - before} unit!"

    def slow(self, obs, *, finish):
        half = max(0, self._speed // 2)
        move = random.randint(max(0, half - 1), half + 1)
        d = self._distance_to_obstacle(obs)
        before = self._position
        if d is not None and move >= d:
            self._position = self._cap(obs + 1, finish)
            return f"{self._name} slowly dodges the obstacle and moves {self._position - before} units!"
        self._position = self._cap(self._position + move, finish)
        return f"{self._name} slowly moves {move} units!"

    def __str__(self):
        return f"{self._name} [Position - {self._position}, Energy - {self._energy}]"

    @abstractmethod
    def special_move(self, obs, *, finish) -> str:
        pass
