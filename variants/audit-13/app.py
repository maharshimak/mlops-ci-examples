"""
Simple Python application for MLOps Final Exam
Students will write unit tests for these functions
"""

def calculate_average(numbers):
    if not isinstance(numbers, list):
        raise TypeError('Input must be a list')
    if len(numbers) == 0:
        raise ValueError('Cannot calculate average of empty list')
    return sum(numbers) / len(numbers)

def is_palindrome(text):
    if not isinstance(text, str):
        raise TypeError('Input must be a string')
    cleaned = text.replace(' ', '').lower()
    return cleaned == cleaned[::-1]

def factorial(n):
    if not isinstance(n, int):
        raise TypeError('Input must be an integer')
    if n < 0:
        raise ValueError('Factorial is not defined for negative numbers')
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def filter_even_numbers(numbers):
    if not isinstance(numbers, list):
        raise TypeError('Input must be a list')
    return [num for num in numbers if isinstance(num, int) and num % 2 == 0]

def main():
    print('MLOps Final Exam - Python Application')
    print('==================================================')
    numbers = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    print(f'\nNumbers: {numbers}')
    print(f'Average: {calculate_average(numbers)}')
    print(f'Even numbers: {filter_even_numbers(numbers)}')
    text = 'A man a plan a canal Panama'
    print(f"\nText: '{text}'")
    print(f'Is palindrome: {is_palindrome(text)}')
    n = 5
    print(f'\nFactorial of {n}: {factorial(n)}')
    print('\nApplication is running successfully!')
    return 0

if __name__ == '__main__':
    main()
