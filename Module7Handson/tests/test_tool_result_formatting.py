from app.services.tool_result_formatter import (
    ToolResultFormatter,
)


def test_tool_result_formatting():

    success_result = ToolResultFormatter.success(
        {
            "city": "Chennai",
            "temperature": 32,
            "unit": "Celsius",
        }
    )

    failure_result = ToolResultFormatter.failure(
        "Unable to retrieve weather."
    )

    print("\nSuccess Result:")
    print(success_result)

    print("\nFailure Result:")
    print(failure_result)


if __name__ == "__main__":
    test_tool_result_formatting()