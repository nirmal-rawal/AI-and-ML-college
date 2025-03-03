def main():
    """
    Main function to handle user input and perform conversions.
    """
    print("Welcome to the Unit Converter!")
    print("Please select the type of conversion:")
    print("1. Length")
    print("2. Weight")
    print("3. Volume")

    try:
        # Prompt user to select conversion type
        conversion_type = int(input("Enter the number corresponding to your choice: "))

        if conversion_type not in [1, 2, 3]:
            print("Invalid choice. Please enter a valid number.")
            return

        # Prompt user to input the value to be converted
        value = float(input("Enter the value to be converted: "))

        if conversion_type == 1:
            # Length conversion
            print("Select length conversion:")
            print("1. Meters (m) to Feet (ft)")
            print("2. Feet (ft) to Meters (m)")
            length_choice = int(input("Enter your choice: "))

            if length_choice == 1:
                result = convert_length(value, 'm', 'ft')
                print(f"{value} meters is equal to {result:.2f} feet.")
            elif length_choice == 2:
                result = convert_length(value, 'ft', 'm')
                print(f"{value} feet is equal to {result:.2f} meters.")
            else:
                print("Invalid choice for length conversion.")

        elif conversion_type == 2:
            # Weight conversion
            print("Select weight conversion:")
            print("1. Kilograms (kg) to Pounds (lbs)")
            print("2. Pounds (lbs) to Kilograms (kg)")
            weight_choice = int(input("Enter your choice: "))

            if weight_choice == 1:
                result = convert_weight(value, 'kg', 'lbs')
                print(f"{value} kilograms is equal to {result:.2f} pounds.")
            elif weight_choice == 2:
                result = convert_weight(value, 'lbs', 'kg')
                print(f"{value} pounds is equal to {result:.2f} kilograms.")
            else:
                print("Invalid choice for weight conversion.")

        elif conversion_type == 3:
            # Volume conversion
            print("Select volume conversion:")
            print("1. Liters (L) to Gallons (gal)")
            print("2. Gallons (gal) to Liters (L)")
            volume_choice = int(input("Enter your choice: "))

            if volume_choice == 1:
                result = convert_volume(value, 'L', 'gal')
                print(f"{value} liters is equal to {result:.2f} gallons.")
            elif volume_choice == 2:
                result = convert_volume(value, 'gal', 'L')
                print(f"{value} gallons is equal to {result:.2f} liters.")
            else:
                print("Invalid choice for volume conversion.")

    except ValueError as e:
        # Handle invalid input (non-numeric values)
        print(f"Error: {e}. Please enter a valid number.")


def convert_length(value, from_unit, to_unit):
    """
    Converts a length value from one unit to another.

    Parameters:
    value (float): The value to be converted.
    from_unit (str): The unit to convert from ('m' for meters, 'ft' for feet).
    to_unit (str): The unit to convert to ('m' for meters, 'ft' for feet).

    Returns:
    float: The converted value.
    """
    if from_unit == 'm' and to_unit == 'ft':
        return value * 3.28084
    elif from_unit == 'ft' and to_unit == 'm':
        return value / 3.28084
    else:
        raise ValueError("Unsupported length conversion units.")


def convert_weight(value, from_unit, to_unit):
    """
    Converts a weight value from one unit to another.

    Parameters:
    value (float): The value to be converted.
    from_unit (str): The unit to convert from ('kg' for kilograms, 'lbs' for pounds).
    to_unit (str): The unit to convert to ('kg' for kilograms, 'lbs' for pounds).

    Returns:
    float: The converted value.
    """
    if from_unit == 'kg' and to_unit == 'lbs':
        return value * 2.20462
    elif from_unit == 'lbs' and to_unit == 'kg':
        return value / 2.20462
    else:
        raise ValueError("Unsupported weight conversion units.")


def convert_volume(value, from_unit, to_unit):
    """
    Converts a volume value from one unit to another.

    Parameters:
    value (float): The value to be converted.
    from_unit (str): The unit to convert from ('L' for liters, 'gal' for gallons).
    to_unit (str): The unit to convert to ('L' for liters, 'gal' for gallons).

    Returns:
    float: The converted value.
    """
    if from_unit == 'L' and to_unit == 'gal':
        return value * 0.264172
    elif from_unit == 'gal' and to_unit == 'L':
        return value / 0.264172
    else:
        raise ValueError("Unsupported volume conversion units.")


if __name__ == "__main__":
    main()