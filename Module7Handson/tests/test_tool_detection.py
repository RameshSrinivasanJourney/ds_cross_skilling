from app.models.tool_models import CURRENT_WEATHER_TOOL
from app.services.ollama_service import OllamaService


def test_tool_extraction():

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": "What is the weather in Chennai right now?"
        }
    ]

    response = service.chat_with_tools(
        messages=messages,
        tools=[CURRENT_WEATHER_TOOL],
    )

    tool_calls = response["message"].get("tool_calls", [])

    if not tool_calls:
        print("\nNo tool call generated.")
        return

    for tool_call in tool_calls:

        tool_name = tool_call.function.name
        arguments = tool_call.function.arguments

        print("\nTool Name:")
        print(tool_name)

        print("\nTool Arguments:")
        print(arguments)

        print("\nCity:")
        print(arguments.get("city"))


if __name__ == "__main__":
    test_tool_extraction()