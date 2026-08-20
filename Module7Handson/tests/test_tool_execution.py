from app.models.tool_models import CURRENT_WEATHER_TOOL
from app.services.ollama_service import OllamaService
from app.tools.tool_registry import TOOL_REGISTRY


def test_tool_execution():

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

        print("\nArguments:")
        print(arguments)

        tool_function = TOOL_REGISTRY.get(tool_name)

        if tool_function is None:
            print("\nTool not found!")
            return

        print("\nExecuting Tool...")

        result = tool_function(**arguments)

        print("\nTool Result:")
        print(result)


if __name__ == "__main__":
    test_tool_execution()