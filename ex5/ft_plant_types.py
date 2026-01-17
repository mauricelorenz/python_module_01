#!/usr/bin/env python3

class Plant:
    """Represents a Plant."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a new Plant.

        Args:
            name: The name of the Plant
            height: The height in cm
            age: The age in days
        """
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Represents a Flower."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a new Flower.

        Args:
            name: The name of the Flower
            height: The height in cm
            age: The age in days
            color: The color of the Flower
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Print a message that the Flower is blooming."""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Represents a Tree."""

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Initialize a new Tree.

        Args:
            name: The name of the Tree
            height: The height in cm
            age: The age in days
            trunk_diameter: The trunk diameter in cm
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Print the shade area provided by this Tree in square meters."""
        print(f"{self.name} provides {int(self.trunk_diameter * 1.56)} "
              "square meters of shade")


class Vegetable(Plant):
    """Represents a Vegetable."""

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """Initialize a new Vegetable.

        Args:
            name: The name of the Vegetable
            height: The height in cm
            age: The age in days
            harvest_season: The season when the Vegetable is harvested
            nutritional_value: The most important nutrient of the Vegetable
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


def main() -> None:
    """Run the main program."""
    rose = Flower("Rose", 25, 30, "red")
    lily = Flower("Lily", 30, 50, "white")
    oak = Tree("Oak", 500, 1825, 50)
    spruce = Tree("Spruce", 1200, 2950, 40)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 30, 50, "spring", "vitamin A")
    flowers = [rose, lily]
    trees = [oak, spruce]
    vegetables = [tomato, carrot]
    print("=== Garden Plant Types ===\n")
    for flower in flowers:
        print(f"{flower.name} ({type(flower).__name__}): {flower.height}cm, "
              f"{flower.age} days, {flower.color} color")
        flower.bloom()
    print()
    for tree in trees:
        print(f"{tree.name} ({type(tree).__name__}): {tree.height}cm, "
              f"{tree.age} days, {tree.trunk_diameter}cm diameter")
        tree.produce_shade()
    print()
    for vegetable in vegetables:
        print(f"{vegetable.name} ({type(vegetable).__name__}): "
              f"{vegetable.height}cm, {vegetable.age} days, "
              f"{vegetable.harvest_season} harvest")
        print(f"{vegetable.name} is rich in {vegetable.nutritional_value}")


if __name__ == "__main__":
    main()
