from app.models.tool_models import (
    CURRENT_WEATHER_TOOL,
    CALCULATOR_TOOL,
)
from app.services.ollama_service import OllamaService


def test_parallel_tool_calls():

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": (
                "What is the weather in Chennai and "
                "calculate 25 multiplied by 4."
            )
        }
    ]

    response = service.chat_with_tools(
        messages=messages,
        tools=[
            CURRENT_WEATHER_TOOL,
            CALCULATOR_TOOL,
        ],
    )

    print("\nUser Question:")
    print(messages[0]["content"])

    tool_calls = response["message"].get(
        "tool_calls",
        []
    )

    print("\nNumber of Tool Calls:")
    print(len(tool_calls))

    for index, tool_call in enumerate(
        tool_calls,
        start=1
    ):
        print(f"\nTool Call {index}:")
        print(f"Name: {tool_call.function.name}")
        print(f"Arguments: {tool_call.function.arguments}")


if __name__ == "__main__":
    test_parallel_tool_calls()