from app.tools.calculator_tool import calculate


def test_tool_error_handling():

    arguments = {
        "a": "invalid-value",
        "b": 2,
        "operation": "multiply",
    }

    print("\nExecuting Calculator:")
    print(arguments)

    try:

        result = calculate(**arguments)

        print("\nTool Result:")
        print(result)

    except Exception as exc:

        result = {
            "status": "failed",
            "error": str(exc),
        }

        print("\nTool Error:")
        print(result)


if __name__ == "__main__":
    test_tool_error_handling()