#!/usr/bin/env python3

class SecurePlant:
    """Represents a Plant with data encapsulation and validation."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a new Plant.

        Args:
            name: The name of the Plant
            height: The height in cm
            age: The age in days
        """
        self.name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {self.name}")

    def set_height(self, height: int) -> None:
        """Set the height of an existing Plant.

        Args:
            height: The height in cm (must not be negative)
        """
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        """Set the age of an existing Plant.

        Args:
            age: The age in days (must not be negative)
        """
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        """Get the height of a Plant.

        Returns:
            The height in cm
        """
        return self.__height

    def get_age(self) -> int:
        """Get the age of a Plant.

        Returns:
            The age in days
        """
        return self.__age


def main() -> None:
    """Run the main program."""
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 20, 25)
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-26)
    print()
    print(f"Current plant: {rose.name} ({rose.get_height()}cm, "
          f"{rose.get_age()} days)")


if __name__ == "__main__":
    main()
