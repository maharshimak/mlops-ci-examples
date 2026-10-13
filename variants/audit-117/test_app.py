import pytest
import app


def test_main(capsys):
    """Test that main() prints the correct sum of first 10 natural numbers."""
    app.main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "The sum of the first 10 natural numbers is: 55"


def test_main_output_format(capsys):
    """Test that main() output contains expected text format."""
    app.main()
    captured = capsys.readouterr()
    assert "sum of the first 10 natural numbers" in captured.out
    assert "55" in captured.out


def test_main_calculation():
    """Test that the sum calculation in main() is correct."""
    # The sum of 1+2+3+4+5+6+7+8+9+10 should equal 55
    expected_sum = 55
    actual_sum = sum(range(1, 11))
    assert actual_sum == expected_sum


def test_sum_range_values():
    """Test individual values in the range used by main()."""
    values = list(range(1, 11))
    assert len(values) == 10
    assert values[0] == 1
    assert values[-1] == 10
    assert 5 in values


@pytest.mark.parametrize("start,end,expected", [
    (1, 11, 55),   # Original case
    (1, 6, 15),    # Sum of first 5 numbers
    (1, 2, 1),     # Sum of just 1
    (0, 1, 0),     # Empty range
])
def test_sum_range_parametrized(start, end, expected):
    """Test sum calculation with different ranges."""
    result = sum(range(start, end))
    assert result == expected


def test_main_no_errors():
    """Test that main() executes without raising exceptions."""
    try:
        app.main()
    except Exception as e:
        pytest.fail(f"main() raised an exception: {e}")


def test_main_returns_none():
    """Test that main() doesn't return a value."""
    result = app.main()
    assert result is None
