def garden_operations() -> None:
    """
    Demonstrates common Python errors in a garden program:
    ValueError, ZeroDivisionError, FileNotFoundError, KeyError,
    and how to catch multiple errors at once.
    """
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    try:
        print("Testing ZeroDivisionError... ")
        1 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    try:
        print("Testing KeyError...")
        my_dict = {}
        my_dict["missing\\_plant"]
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")
    try:
        print("Testing multiple errors together...")
        int("oops")
        1 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
