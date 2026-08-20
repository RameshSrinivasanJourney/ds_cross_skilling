from app.models.tool_models import WEATHER_TOOL
from app.services.ollama_service import OllamaService


def test_weather_tool_call():
    """Test whether Ollama identifies the weather tool."""

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": "What is the weather in Chennai?"
        }
    ]

    response = service.chat_with_tools(
        messages=messages,
        tools=[WEATHER_TOOL],
    )

    print("\nFull Ollama response:")
    print(response)

    print("\nMessage:")
    print(response["message"])

    if response["message"].get("tool_calls"):
        print("\nTool calls:")
        print(response["message"]["tool_calls"])
    else:
        print("\nNo tool call was generated.")


if __name__ == "__main__":
    test_weather_tool_call()