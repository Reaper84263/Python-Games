"""
PlateDecorator - abstract decorator that wraps a Plate.
"""
from abc import ABC
from plate import Plate


class PlateDecorator(Plate, ABC):
    def __init__(self, p: Plate) -> None:
        self._plate: Plate = p

    # Delegate base behavior to the wrapped plate. Concrete food
    # classes will extend/modify these where needed.
    def description(self) -> str:
        return self._plate.description()

    def area(self) -> int:
        return self._plate.area()

    def weight(self) -> int:
        return self._plate.weight()

    def count(self) -> int:
        return self._plate.count()

    # Utility for subclasses to append food names cleanly
    def _append_food(self, food_name: str) -> str:
        base = self._plate.description()
        if " with " in base:
            return f"{base} and {food_name}"
        else:
            return f"{base} with {food_name}"
