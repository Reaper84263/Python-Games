"""
LargePlate - concrete plate
Large flimsy 12-inch paper plate:
    - Area capacity: 113 square inches
    - Weight capacity: 24 ounces (flimsier)
"""
from plate import Plate


class LargePlate(Plate):
    def __init__(self) -> None:
        self._area_cap = 113
        self._weight_cap = 24

    def description(self) -> str:
        return "Flimsy 12 inch paper plate"

    def area(self) -> int:
        return self._area_cap

    def weight(self) -> int:
        return self._weight_cap

    def count(self) -> int:
        return 0
