from pydantic import BaseModel


class CalculationResult(BaseModel):
    operation: str
    a: float
    b: float
    result: float


def multiply_structured(
    a: float,
    b: float,
) -> CalculationResult:
    """Multiply two numbers and return structured output."""

    return CalculationResult(
        operation="multiply",
        a=a,
        b=b,
        result=a * b,
    )