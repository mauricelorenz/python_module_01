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

    def grow(self, amount: int) -> None:
        """Increment the height of the Plant.

        Args:
            amount: height in cm to be added
        """
        self.height += amount

    def increment_age(self, amount: int) -> None:
        """Increment the age of the Plant.

        Args:
            amount: age in days to be added
        """
        self.age += amount

    def get_info(self) -> str:
        """Give an overview about the Plant.

        Returns:
            {name}: {height}cm, {age} days old
        """
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main() -> None:
    """Run the main program."""
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    plants = [rose, sunflower, cactus]
    day_start = 1
    day_end = 7
    print(f"=== Day {day_start} ===")
    for plant in plants:
        print(plant.get_info())
        plant.grow(day_end - day_start)
        plant.increment_age(day_end - day_start)
    print(f"=== Day {day_end} ===")
    for plant in plants:
        print(plant.get_info())
        print(f"Growth this week: +{day_end - day_start}cm")


if __name__ == "__main__":
    main()
