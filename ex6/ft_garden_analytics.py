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

    @classmethod
    def create_garden_network(cls, owners: list) -> list:
        owners_objects = []
        for owner in owners:
            owners_objects.append(cls(owner))
        return owners_objects

    class GardenStats:

        @staticmethod
        def print_garden_report(garden: "GardenManager") -> None:
            print(f"=== {garden.owner}'s Garden Report ===")
            for plant in garden.plants:
                print(f"- {plant.name}: {plant.height}cm", end="")
                if isinstance(plant, FloweringPlant):
                    print(f", {plant.color} flowers "
                          f"{"(blooming)" if plant.blooming else " "}", end="")
                if isinstance(plant, PrizeFlower):
                    print(f", Prize points: {plant.prize_points}", end="")
                print()


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
    owners = GardenManager.create_garden_network(["Alice", "Bob"])
    oak = Plant("Oak Tree", 101)
    rose = FloweringPlant("Rose", 26, "red", True)
    sunflower = PrizeFlower("Sunflower", 51, "yellow", True, 10)
    for plant in [oak, rose, sunflower]:
        owners[0].add_plant(plant)
    print()
    owners[0].help_all_grow(1)
    print()
    GardenManager.GardenStats.print_garden_report(owners[0])


if __name__ == "__main__":
    main()
