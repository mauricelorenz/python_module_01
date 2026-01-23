#!/usr/bin/env python3

class GardenManager:
    plants: list["Plant"]

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []

    def add_plant(self, plant: "Plant") -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_all_grow(self, amount: int) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(amount)

    def create_garden_network(self) -> None:
        pass

    class GardenStats:
        pass


class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self, amount: int):
        self.height += amount
        print(f"{self.name} grew {amount}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int,
                 color: str, blooming: bool) -> None:
        super().__init__(name, height)
        self.color = color
        self.blooming = blooming


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str,
                 blooming: bool, prize_points: int) -> None:
        super().__init__(name, height, color, blooming)
        self.prize_points = prize_points


def main() -> None:
    """Run the main program."""
    print("=== Garden Management System Demo ===\n")
    alice = GardenManager("Alice")
    oak = Plant("Oak Tree", 101)
    rose = FloweringPlant("Rose", 26, "red", True)
    sunflower = PrizeFlower("Sunflower", 51, "yellow", True, 10)
    for plant in [oak, rose, sunflower]:
        alice.add_plant(plant)
    print()
    alice.help_all_grow(1)


if __name__ == "__main__":
    main()
