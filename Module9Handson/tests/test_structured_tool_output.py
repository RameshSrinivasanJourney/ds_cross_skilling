from app.tools.structured_calculator_tool import (
    multiply_structured,
)


def test_structured_tool_output():

    result = multiply_structured(
        a=25,
        b=4,
    )

    print("\nStructured Result:")
    print(result)

    print("\nResult Type:")
    print(type(result))

    print("\nCalculated Value:")
    print(result.result)


if __name__ == "__main__":
    test_structured_tool_output()