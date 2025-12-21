class GardenError(Exception):
    """
    Base class for garden-related errors
    """
    pass


class PlantError(GardenError):
    """
    Raised when a plant has a problem
    """
    def __init__(self):
        super().__init__("The tomato plant is wilting!")


class WaterError(GardenError):
    """
    Raised when there is not enough water
    """
    def __init__(self):
        super().__init__("Not enough water in the tank!")


def check_plant(is_healthy: bool) -> None:
    """
    Raise PlantError if the plant is unhealthy
    """
    if not is_healthy:
        raise PlantError()


def check_water(has_water: bool) -> None:
    """
    Raise WaterError if there is no water
    """
    if not has_water:
        raise WaterError()


def check_errors() -> None:
    """
    Catch specific type errors and display them
    Demonstrate that catching GardenError catches all garden-related errors
    """
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        check_plant(False)
    except PlantError as plant_error:
        print(f"Caught PlantError: {plant_error}\n")
    try:
        print("Testing WaterError...")
        check_water(False)
    except WaterError as water_error:
        print(f"Caught WaterError: {water_error}\n")
    print("Testing catching all garden errors...")
    garden_checks = [(check_plant, False), (check_water, False)]
    for check, condition in garden_checks:
        try:
            check(condition)
        except GardenError as err:
            print(f"Caught a garden error: {err}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    check_errors()
