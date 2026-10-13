import pytest
from math_ops import divide, multiply, add, subtract

def test_basic_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(10, 0)

def test_divide_negative():
    assert divide(-10, 2) == -5
    assert divide(10, -2) == -5
    assert divide(-10, -2) == 5

def test_basic_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-3, 4) == -12
    assert multiply(3, -4) == -12
    assert multiply(-3, -4) == 12

def test_multiply_by_zero():
    assert multiply(3, 0) == 0
    assert multiply(0, 4) == 0
    assert multiply(0, 0) == 0
    
def test_basic_add():
    assert add(3, 4) == 7
    assert add(-3, 4) == 1
    assert add(3, -4) == -1
    assert add(-3, -4) == -7

def test_basic_subtract():
    assert subtract(10, 4) == 6
    assert subtract(-10, 4) == -14
    assert subtract(10, -4) == 14
    assert subtract(-10, -4) == -6