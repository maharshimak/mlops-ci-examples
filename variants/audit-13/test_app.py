"""
Unit tests for MLOps Final Exam
Tests cover all functions in app.py with normal cases, edge cases, and error handling.
"""

import pytest
from app import calculate_average, is_palindrome, factorial, filter_even_numbers, main

class TestCalculateAverage:
    """Test cases for calculate_average function"""
    
    def test_average_positive_numbers(self):
        assert calculate_average([1, 2, 3, 4, 5]) == 3.0
        
    def test_average_negative_numbers(self):
        assert calculate_average([-1, -2, -3, -4, -5]) == -3.0
        
    def test_average_single_number(self):
        assert calculate_average([10]) == 10.0
        
    def test_average_empty_list_raises_error(self):
        with pytest.raises(ValueError):
            calculate_average([])
            
    def test_average_invalid_input_raises_error(self):
        with pytest.raises(TypeError):
            calculate_average('not a list')


class TestIsPalindrome:
    """Test cases for is_palindrome function"""
    
    def test_simple_palindrome(self):
        assert is_palindrome('racecar') is True
        
    def test_palindrome_with_spaces(self):
        assert is_palindrome('A man a plan a canal Panama') is True
        
    def test_not_palindrome(self):
        assert is_palindrome('hello') is False
        
    def test_empty_string(self):
        assert is_palindrome('') is True
        
    def test_palindrome_invalid_input_raises_error(self):
        with pytest.raises(TypeError):
            is_palindrome(12345)


class TestFactorial:
    """Test cases for factorial function"""
    
    def test_factorial_zero(self):
        assert factorial(0) == 1
        
    def test_factorial_one(self):
        assert factorial(1) == 1
        
    def test_factorial_positive_number(self):
        assert factorial(5) == 120
        
    def test_factorial_negative_raises_error(self):
        with pytest.raises(ValueError):
            factorial(-1)
            
    def test_factorial_invalid_input_raises_error(self):
        with pytest.raises(TypeError):
            factorial(3.5)


class TestFilterEvenNumbers:
    """Test cases for filter_even_numbers function"""
    
    def test_filter_mixed_numbers(self):
        assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
        
    def test_filter_all_odd(self):
        assert filter_even_numbers([1, 3, 5, 7]) == []
        
    def test_filter_all_even(self):
        assert filter_even_numbers([2, 4, 6, 8]) == [2, 4, 6, 8]
        
    def test_filter_empty_list(self):
        assert filter_even_numbers([]) == []
        
    def test_filter_invalid_input_raises_error(self):
        with pytest.raises(TypeError):
            filter_even_numbers('not a list')


def test_integration():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = filter_even_numbers(numbers)
    assert even_numbers == [2, 4, 6, 8, 10]
    avg = calculate_average(even_numbers)
    assert avg == 6.0
    
    assert is_palindrome('racecar') is True
    assert factorial(len('racecar')) == 5040


def test_main(capsys):
    result = main()
    assert result == 0
    captured = capsys.readouterr()
    assert 'MLOps Final Exam' in captured.out
    assert 'Average' in captured.out
    assert 'Even numbers' in captured.out
    assert 'Is palindrome' in captured.out
    assert 'Factorial' in captured.out
    assert 'Application is running successfully!' in captured.out


def test_filter_even_with_non_integers():
    assert filter_even_numbers([1, 2.5, 'hello', 4, None, 6]) == [4, 6]
