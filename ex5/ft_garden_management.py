class GardenError(Exception):
    """
    Base exception for garden-related errors.
    """
    pass


class InvalidPlantError(GardenError):
    """
    Raised when a plant has an invalid name.
    """
    def __init__(self):
        super().__init__("Plant name cannot be empty!")


class LevelError(GardenError):
    """
    Raised when a plant's water or sunlight level is out of range.
    """
    def __init__(self, message):
        super().__init__(message)


class Plant:
    """
    Represents a plant with a name, water level, and sunlight hours.
    """
    def __init__(
            self, name: str, water_level: int, sunlight_hours: int
            ) -> None:
        self.name = name
        self.water = water_level
        self.sun = sunlight_hours


class GardenManager:
    """
    Manages a collection of plants, adding, watering, and checking health.
    Demonstrates proper error handling with try/except/finally blocks.
    """
    def __init__(self) -> None:
        self.plants = []

    def add_plant(
            self, plant_name: str, water_level: int, sunlight_hours: int
            ) -> None:
        """
        Adds a plant to the garden.
        Raises InvalidPlantError if the plant name is empty.
        """
        try:
            if not plant_name:
                raise InvalidPlantError()
            plant = Plant(plant_name, water_level, sunlight_hours)
            self.plants.append(plant)
            print(f"Added {plant_name} successfully")
        except InvalidPlantError as error:
            print(f"Error adding plant: {error}")

    def water_plants(self) -> None:
        """
        Waters all plants in the garden.
        Uses a finally block to ensure cleanup always occurs.
        """
        print("Opening watering system")
        try:
            for plant in self.plants:
                if plant.name is None:
                    raise InvalidPlantError("invalid plant")
                print(f"Watering {plant.name}- success")
        except InvalidPlantError as error:
            print(f"Error: {error}")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plant_health(self, plant: Plant) -> None:
        """
        Checks the health of a plant based on water and sunlight levels.
        Raises WaterLevelError for out-of-range values.
        """
        try:
            if plant.water > 10:
                raise LevelError(
                    f"Water level {plant.water} is too high (max 10)"
                    )
            if plant.water < 1:
                raise LevelError(
                    f"Water level {plant.water} is too low (min 1)"
                    )
            if plant.sun > 12:
                raise LevelError(
                    f"Sunlight hours {plant.sun} is too high (max 12)"
                    )
            if plant.sun < 2:
                raise LevelError(
                    f"Sunlight hours {plant.sun} is too low (min 2)"
                    )
            print(
                f"{plant.name}: healthy "
                f"(water: {plant.water}, sun: {plant.sun})")
        except LevelError as error:
            print(f"Error checking {plant.name}: {error}")


def check_garden_manager() -> None:
    """
    Demonstrates the GardenManager system.
    Adds plants, waters them, checks health, and handles errors.
    """
    manager = GardenManager()
    print("=== Garden Management System ===\n")

    print("Adding plants to garden...")
    manager.add_plant("tomato", 5, 8)
    manager.add_plant("lettuce", 15, 8)
    manager.add_plant(None, 5, 8)

    print("\nWatering plants...")
    manager.water_plants()

    print("Checking plant health...")
    for plant in manager.plants:
        manager.check_plant_health(plant)

    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as error:
        print(f"Caught GardenError: {error}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    check_garden_manager()
