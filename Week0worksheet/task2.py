def calculate_sum(numbers):
    """
    Calculates the sum of a list of numbers.

    Parameters:
    numbers (list): A list of numeric values.

    Returns:
    float: The sum of the numbers.
    """
    return sum(numbers)


def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.

    Parameters:
    numbers (list): A list of numeric values.

    Returns:
    float: The average of the numbers.
    """
    return sum(numbers) / len(numbers)


def find_maximum(numbers):
    """
    Finds the maximum value in a list of numbers.

    Parameters:
    numbers (list): A list of numeric values.

    Returns:
    float: The maximum value in the list.
    """
    return max(numbers)


def find_minimum(numbers):
    """
    Finds the minimum value in a list of numbers.

    Parameters:
    numbers (list): A list of numeric values.

    Returns:
    float: The minimum value in the list.
    """
    return min(numbers)


def main():
    """
    Main function to handle user input and perform mathematical operations.
    """
    print("Welcome to the Math Operations Program!")
    print("Please select an operation:")
    print("1. Sum")
    print("2. Average")
    print("3. Maximum")
    print("4. Minimum")

    try:
        # Prompt user to select an operation
        operation = int(input("Enter the number corresponding to your choice: "))

        if operation not in [1, 2, 3, 4]:
            print("Invalid choice. Please select a number between 1 and 4.")
            return

        # Prompt user to input a list of numbers
        user_input = input("Enter a list of numbers separated by commas: ").strip()
        
        #check if the user input is empty
        if not user_input:
            raise ValueError("Empty input. Please enter at least one number.")
        
        if user_input.count(",")==False or len(user_input.split(","))<2:
            print("Numbers should be separated by commas, and you must enter at least two numbers.")

        # Convert input string to a list of floats
        numbers = [float(num) for num in user_input.split()]

        if operation == 1:
            # Calculate sum
            result = calculate_sum(numbers)
            print(f"The sum of the numbers is: {result:.2f}")

        elif operation == 2:
            # Calculate average
            result = calculate_average(numbers)
            print(f"The average of the numbers is: {result:.2f}")

        elif operation == 3:
            # Find maximum
            result = find_maximum(numbers)
            print(f"The maximum number is: {result:.2f}")

        elif operation == 4:
            # Find minimum
            result = find_minimum(numbers)
            print(f"The minimum number is: {result:.2f}")

    except ValueError as e:
        # Handle invalid input (non-numeric values or empty lists)
        print(f"Error: {e}. Please enter valid numbers.")


if __name__ == "__main__":
    main()