def calculate(a: float, b: float, operation: str) -> dict:
    """Perform a basic mathematical calculation."""

    a = float(a)
    b = float(b)

    if operation == "add":
        result = a + b

    elif operation == "subtract":
        result = a - b

    elif operation == "multiply":
        result = a * b

    elif operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero.")

        result = a / b

    else:
        raise ValueError(
            f"Unsupported operation: {operation}"
        )

    return {
        "a": a,
        "b": b,
        "operation": operation,
        "result": result,
    }