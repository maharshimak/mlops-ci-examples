def divide(a, b):
    """Returns the division of a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def multiply(a, b):
    """Returns the multiplication of a and b."""
    return a * b

def add(a, b):
    """Returns the addition of a and b."""
    return a + b

def subtract(a, b):
    """Returns the subtraction of b from a."""
    return a - b

def calculator(method: str, a: float, b: float) -> float:
    """Performs a calculation based on the method provided."""
    if method == "add":
        return add(a, b)
    elif method == "subtract":
        return subtract(a, b)
    elif method == "multiply":
        return multiply(a, b)
    elif method == "divide":
        return divide(a, b)
    else:
        raise ValueError(f"Unknown method: {method}")