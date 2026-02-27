"""
Green Beans - concrete decorator
Subtracts its area/weight and increments the item count.
Suggested values from the spec.
"""
from plate_decorator import PlateDecorator


class GreenBeans(PlateDecorator):
    _AREA = 20
    _WEIGHT = 3
    _FOOD_NAME = "Green Beans"

    def description(self) -> str:
        return self._append_food(self._FOOD_NAME)

    def area(self) -> int:
        return self._plate.area() - self._AREA

    def weight(self) -> int:
        return self._plate.weight() - self._WEIGHT

    def count(self) -> int:
        return self._plate.count() + 1
