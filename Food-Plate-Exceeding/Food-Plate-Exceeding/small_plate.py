from plate import Plate


class SmallPlate(Plate):
    def __init__(self) -> None:
        self._area_cap = 78
        self._weight_cap = 32

    def description(self) -> str:
        return "Sturdy 10 inch paper plate"

    def area(self) -> int:
        return self._area_cap

    def weight(self) -> int:
        return self._weight_cap

    def count(self) -> int:
        return 0
