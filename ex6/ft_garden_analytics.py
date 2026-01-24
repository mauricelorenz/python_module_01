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
            growth = 0
            plant_types = [0, 0, 0]
            print(f"=== {garden.owner}'s Garden Report ===")
            for plant in garden.plants:
                plant_types[0] += 1
                print(f"- {plant.name}: {plant.height}cm", end="")
                if isinstance(plant, FloweringPlant):
                    plant_types[1] += 1
                    print(f", {plant.color} flowers "
                          f"{"(blooming)" if plant.blooming else " "}", end="")
                if isinstance(plant, PrizeFlower):
                    plant_types[2] += 1
                    print(f", Prize points: {plant.prize_points}", end="")
                print()
                growth += plant.height - plant.initial_height
            print(f"Plants added: {len(garden.plants)}, "
                  f"Total growth: {growth}cm")
            print(f"Plant types: {plant_types[0] - plant_types[1]} "
                  f"regular, {plant_types[1] - plant_types[2]} "
                  f"flowering, {plant_types[2]} prize flowers")

        @staticmethod
        def validate_height(garden: "GardenManager") -> bool:
            for plant in garden.plants:
                if plant.height < 0:
                    return False
            return True

        @staticmethod
        def get_garden_score(garden: "GardenManager") -> int:
            score = 0
            for plant in garden.plants:
                score += plant.height
                if isinstance(plant, PrizeFlower):
                    score += plant.prize_points * 4
            return score


class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height
        self.initial_height = height

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
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, "yellow", True, 10)
    for plant in [oak, rose, sunflower]:
        owners[0].add_plant(plant)
    spruce = Plant("Spruce Tree", 82)
    lily = FloweringPlant("Lily", 10, "white", True)
    for plant in [spruce, lily]:
        owners[1].add_plant(plant)
    print()
    owners[0].help_all_grow(1)
    print()
    stats = GardenManager.GardenStats
    stats.print_garden_report(owners[0])
    print()
    print(f"Height validation test: {stats.validate_height(owners[0])}")
    print(f"Garden scores - Alice: {stats.get_garden_score(owners[0])}, "
          f"Bob: {stats.get_garden_score(owners[1])}")
    print(f"Total gardens managed: {len(owners)}")


if __name__ == "__main__":
    main()
