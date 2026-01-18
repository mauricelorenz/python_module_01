#!/usr/bin/env python3

class GardenManager:
    def __init__(self, owner: str) -> None:
        self.owner = owner

    def create_garden_network(self) -> None:
        pass

    class GardenStats:
        pass


class Plant:
    def __init__(self, name: str) -> None:
        self.name = name


class FloweringPlant(Plant):
    def __init__(self, name: str) -> None:
        super().__init__(name)


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str) -> None:
        super().__init__(name)


def main() -> None:
    """Run the main program."""


if __name__ == "__main__":
    main()
