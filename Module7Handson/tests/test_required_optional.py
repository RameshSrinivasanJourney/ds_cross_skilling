from app.models.tool_models import WEATHER_FORECAST_OPTIONAL_TOOL
from app.services.ollama_service import OllamaService


def test_required_parameter_only():

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": (
                "Give me the weather forecast for Chennai "
                "for the next 5 days in Celsius."
            )
        }
    ]

    response = service.chat_with_tools(
        messages=messages,
        tools=[WEATHER_FORECAST_OPTIONAL_TOOL],
    )

    print("\nUser Question:")
    print(messages[0]["content"])

    print("\nTool Call:")

    tool_calls = response["message"].get("tool_calls", [])

    if tool_calls:
        for tool_call in tool_calls:
            print(tool_call)
    else:
        print("No tool call generated.")


if __name__ == "__main__":
    test_required_parameter_only()