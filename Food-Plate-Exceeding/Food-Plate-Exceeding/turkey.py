"""
Turkey - concrete decorator
Subtracts its area/weight and increments the item count.
Suggested values from the spec.
"""
from plate_decorator import PlateDecorator


class Turkey(PlateDecorator):
    _AREA = 15
    _WEIGHT = 4
    _FOOD_NAME = "Turkey"

    def description(self) -> str:
        return self._append_food(self._FOOD_NAME)

    def area(self) -> int:
        return self._plate.area() - self._AREA

    def weight(self) -> int:
        return self._plate.weight() - self._WEIGHT

    def count(self) -> int:
        return self._plate.count() + 1
