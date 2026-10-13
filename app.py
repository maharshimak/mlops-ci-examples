"""
Simple Python application for MLOps Final Exam
Students will write unit tests for these functions
"""


def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers: List of numbers

    Returns:
        float: Average of the numbers

    Raises:
        ValueError: If the list is empty
        TypeError: If input is not a list
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if len(numbers) == 0:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)


def is_palindrome(text):
    """
    Check if a string is a palindrome (ignoring case and spaces).

    Args:
        text: String to check

    Returns:
        bool: True if palindrome, False otherwise

    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n: Non-negative integer

    Returns:
        int: Factorial of n

    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def filter_even_numbers(numbers):
    """
    Filter and return only even numbers from a list.

    Args:
        numbers: List of integers

    Returns:
        list: List containing only even numbers

    Raises:
        TypeError: If input is not a list
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    return [num for num in numbers if isinstance(num, int) and num % 2 == 0]


def main():
    """Main function to demonstrate the application"""
    print("MLOps Final Exam - Python Application")
    print("=" * 50)

    # Example usage
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"\nNumbers: {numbers}")
    print(f"Average: {calculate_average(numbers)}")
    print(f"Even numbers: {filter_even_numbers(numbers)}")

    text = "A man a plan a canal Panama"
    print(f"\nText: '{text}'")
    print(f"Is palindrome: {is_palindrome(text)}")

    n = 5
    print(f"\nFactorial of {n}: {factorial(n)}")

    print("\nApplication is running successfully!")
    return 0


if __name__ == "__main__":
    main()
