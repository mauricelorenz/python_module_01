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
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def main() -> None:
    """Run the main program."""
    plants = {"rose": ("Rose", 25, 30),
              "oak": ("Oak", 200, 365),
              "cactus": ("Cactus", 5, 90),
              "sunflower": ("Sunflower", 80, 45),
              "fern": ("Fern", 15, 120)}
    plant_objects = {}
    print("=== Plant Factory Output ===")
    for plant in plants:
        name, height, age = plants[plant]
        plant_objects[plant] = Plant(name, height, age)
    print(f"\nTotal plants created: {len(plant_objects)}")


if __name__ == "__main__":
    main()
