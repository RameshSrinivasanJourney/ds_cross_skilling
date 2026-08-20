from app.models.tool_models import (
    CURRENT_WEATHER_TOOL,
    WEATHER_FORECAST_TOOL,
)
from app.services.ollama_service import OllamaService


def test_tool_selection():

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": "What will the weather be like in Chennai for the next 3 days?"
        }
    ]

    tools = [
        CURRENT_WEATHER_TOOL,
        WEATHER_FORECAST_TOOL,
    ]

    response = service.chat_with_tools(
        messages=messages,
        tools=tools,
    )

    print("\nUser Question:")
    print(messages[0]["content"])

    print("\nSelected Tool:")

    tool_calls = response["message"].get("tool_calls", [])

    if tool_calls:
        for tool_call in tool_calls:
            print(tool_call)
    else:
        print("No tool selected.")


if __name__ == "__main__":
    test_tool_selection()