import json

from app.models.tool_models import CURRENT_WEATHER_TOOL
from app.services.ollama_service import OllamaService
from app.tools.tool_registry import TOOL_REGISTRY


def test_tool_result_return():

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": "What is the weather in Chennai right now?"
        }
    ]

    # First LLM call
    response = service.chat_with_tools(
        messages=messages,
        tools=[CURRENT_WEATHER_TOOL],
    )

    tool_calls = response["message"].get("tool_calls", [])

    if not tool_calls:
        print("\nNo tool call generated.")
        return

    # Add the assistant's tool-call message to the conversation
    messages.append(response["message"])

    for tool_call in tool_calls:

        tool_name = tool_call.function.name
        arguments = tool_call.function.arguments

        print("\nTool Name:")
        print(tool_name)

        print("\nArguments:")
        print(arguments)

        # Find the Python function
        tool_function = TOOL_REGISTRY.get(tool_name)

        if tool_function is None:
            print("\nTool not found!")
            return

        # Execute the tool
        tool_result = tool_function(**arguments)

        print("\nTool Result:")
        print(tool_result)

        # Convert result to JSON string
        tool_content = json.dumps(tool_result)

        # Return result to the conversation
        messages.append(
            {
                "role": "tool",
                "tool_name": tool_name,
                "content": tool_content,
            }
        )

    print("\nMessages sent back to Ollama:")
    for message in messages:
        print(message)

    # Second LLM call
    final_response = service.chat(messages)

    print("\nFinal Ollama Response:")
    print(final_response)


if __name__ == "__main__":
    test_tool_result_return()