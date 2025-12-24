def water_plants(plant_list: list) -> None:
    """
    Display watered plant unless there is an invalid name.
    Raises an error and cleans up resources.

    plant_list: The names of the plants that need to be watered
    """
    print("Opening watering system")
    error_occurred = False
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("invalid plant")
            print(f"Watering {plant}")
    except ValueError:
        print(f"Error: Cannot water {plant} - invalid plant!")
        error_occurred = True
    finally:
        print("Closing watering system (cleanup)")
    if not error_occurred:
        print("Watering completed successfully!\n")


def test_watering_system() -> None:
    """
    Test the watering function with valid and invalid inputs.
    """
    print("Testing normal watering...")
    plant_list = ["tomato", "lettuce", "carrots"]
    water_plants(plant_list)

    print("Testing with error...")
    plant_list = ["tomato", None, "carrots"]
    water_plants(plant_list)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
