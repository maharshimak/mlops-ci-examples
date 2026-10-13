import pytest
from math_ops import divide, multiply, add, subtract, calculator

def test_calculator_operations():
    assert calculator(10, 2, 'add') == 12
    assert calculator(10, 2, 'subtract') == 8
    assert calculator(10, 2, 'multiply') == 20
    assert calculator(10, 2, 'divide') == 5