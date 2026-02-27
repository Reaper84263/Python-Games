"""
Thanksgiving Dinner - Decorator Pattern Game
Authors: Kaleab Daniel and Bryan Giang
Date: Fall 2025
Brief: Let the user add foods to a plate without exceeding the plate's
       area or weight capacity. Uses the Decorator pattern.
"""
import check_input
from typing import Callable
from plate import Plate
from small_plate import SmallPlate
from large_plate import LargePlate
from turkey import Turkey
from stuffing import Stuffing
from potatoes import Potatoes
from green_beans import GreenBeans
from pie import Pie


def examine_plate(p: Plate) -> bool:
    """Show status and hints; return True if plate fails."""
    print(p.description())

    area = p.area()
    weight = p.weight()

    if area <= 0:
        print("Your plate isn't big enough for\nthis much food! Your food spills\nover the edge.")
        return True
    if weight <= 0:
        print("Your plate can't handle this much weight!\nIt bends and everything falls off.")
        return True

    if weight >= 13:
        sturdy = "Strong"
    elif weight >= 7:
        sturdy = "Weak"
    else:
        sturdy = "Bending"

    if area >= 41:
        space = "Plenty"
    elif area >= 21:
        space = "Some"
    else:
        space = "A tiny bit"

    print(f"Sturdiness: {sturdy}")
    print(f"Space available: {space}")
    return False

def choose_plate() -> Plate:
    print("- Thanksgiving Dinner -")
    print("Serve yourself as much food as you\nlike from the buffet, but make sure\nthat your plate will hold without\nspilling everywhere!")
    print("Choose a plate:")
    print("1. Small Sturdy Plate")
    print("2. Large Flimsy Plate")
    choice = check_input.get_int_range("Enter choice: ", 1, 2)
    return SmallPlate() if choice == 1 else LargePlate()

def choose_food() -> int:
    print("1. Turkey")
    print("2. Stuffing")
    print("3. Potatoes")
    print("4. Green Beans")
    print("5. Pie")
    print("6. Quit")
    return check_input.get_int_range("Enter choice: ", 1, 6)

def main():
    plate: Plate = choose_plate()

    options: dict[int, Callable[[Plate], Plate]] = {
        1: lambda p: Turkey(p),
        2: lambda p: Stuffing(p),
        3: lambda p: Potatoes(p),
        4: lambda p: GreenBeans(p),
        5: lambda p: Pie(p)
    }

    while True:
        choice = choose_food()
        if choice == 6:
            print(plate.description())
            print(f"Good job! You made it to the table\nwith {plate.count()} items.")
            print(f"There was still {plate.area()} square inches\nleft on your plate.")
            print(f"Your plate could have held {plate.weight()} more\nounces of food.")
            print("Don't worry, you can always go back\nfor more. Happy Thanksgiving!")
            break

        plate = options[choice](plate)
        if examine_plate(plate):
            break

if __name__ == "__main__":
    main()