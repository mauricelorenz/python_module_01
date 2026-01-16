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


def main() -> None:
    """Run the main program."""
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    plants = [rose, sunflower, cactus]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    main()
