def check_plant_health(
        plant_name: str, water_level: int, sunlight_hours: int
        ) -> None:
    """
    Display if the plant is healthy unless there is an invalid parameter.
    Raises an error and displays a clear message about the error.

    plant_name: Name of the plant cannot be empty
    water_level: How much water the plant has
    sunlight_hours: How many hoours of sunlight has the plant received
    """
    try:
        if not plant_name:
            raise ValueError("Error: Plant name cannot be empty!")

        if water_level > 10:
            raise ValueError(
                f"Error: Water level {water_level} is too high (max 10)"
                )
        if water_level < 1:
            raise ValueError(
                f"Error: Water level {water_level} is too low (min 1)"
                )

        if sunlight_hours > 12:
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} is too high (max 12)"
            )
        if sunlight_hours < 2:
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} is too low (min 2)"
            )

        print(f"Plant '{plant_name}' is healthy!")

    except ValueError as error:
        print(error)


def test_plant_checks() -> None:
    """
    Test the check plant health function with valid and invalid inputs.
    """
    print("\nTesting good values...")
    check_plant_health("tomato", 7, 5)

    print("\nTesting empty plant name...")
    check_plant_health(None, 7, 5)

    print("\nTesting bad water level...")
    check_plant_health("tomato", 15, 5)

    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 7, 0)

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===")
    test_plant_checks()
