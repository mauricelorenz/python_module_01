#!/usr/bin/env python3

class GardenManager:
    """Represents a GardenManager."""

    plants: list["Plant"]

    def __init__(self, owner: str) -> None:
        """Initialize a new GardenManager.

        Args:
            owner: The name of the owner
        """
        self.owner = owner
        self.plants = []

    def add_plant(self, plant: "Plant") -> None:
        """Add a new Plant to GardenManager.

        Args:
            plant: The Plant object to add
        """
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_all_grow(self, amount: int) -> None:
        """Call the grow method on all plants in a GardenManager.

        Args:
            amount: The amount to add to each plant's height
        """
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(amount)

    @classmethod
    def create_garden_network(cls, owners: list) -> list:
        """Create multiple GardenManager instances.

        Args:
            owners: List of owner names for the GardenManager instances

        Returns:
            List of GardenManager instances
        """
        owners_objects = []
        for owner in owners:
            owners_objects.append(cls(owner))
        return owners_objects

    class GardenStats:
        """Helper for generating statistics of a GardenManager instance."""

        @staticmethod
        def print_garden_report(garden: "GardenManager") -> None:
            """Output a statistics overview.

            Args:
                garden: The GardenManager instance to be reported
            """
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
            """Check the height of all plants in a GardenManager instance.

            Args:
                garden: The GardenManager instance to be validated

            Returns:
                True if all heights are valid, False if not
            """
            for plant in garden.plants:
                if plant.height < 0:
                    return False
            return True

        @staticmethod
        def get_garden_score(garden: "GardenManager") -> int:
            """Calculate a score based on heights and prize_points.

            Args:
                garden: The GardenManager instance to be scored

            Returns:
                The calculated score for the GardenManager instance
            """
            score = 0
            for plant in garden.plants:
                score += plant.height
                if isinstance(plant, PrizeFlower):
                    score += plant.prize_points * 4
            return score


class Plant:
    """Represents a Plant."""

    def __init__(self, name: str, height: int) -> None:
        """Initialize a new Plant.

        Args:
            name: The name of the Plant
            height: The height in cm
        """
        self.name = name
        self.height = height
        self.initial_height = height

    def grow(self, amount: int) -> None:
        """Grow the Plant by amount.

        Args:
            amount: The amount to add to the plant's height
        """
        self.height += amount
        print(f"{self.name} grew {amount}cm")


class FloweringPlant(Plant):
    """Represents a FloweringPlant."""

    def __init__(self, name: str, height: int,
                 color: str, blooming: bool) -> None:
        """Initialize a new FloweringPlant.

        Args:
            name: The name of the FloweringPlant
            height: The height in cm
            color: The color of the FloweringPlant
            blooming: Blooming status of the FloweringPlant
        """
        super().__init__(name, height)
        self.color = color
        self.blooming = blooming


class PrizeFlower(FloweringPlant):
    """Represents a PrizeFlower."""

    def __init__(self, name: str, height: int, color: str,
                 blooming: bool, prize_points: int) -> None:
        """Initialize a new PrizeFlower.

        Args:
            name: The name of the PrizeFlower
            height: The height in cm
            color: The color of the PrizeFlower
            blooming: Blooming status of the PrizeFlower
            prize_points: The points the PrizeFlower has won
        """
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
