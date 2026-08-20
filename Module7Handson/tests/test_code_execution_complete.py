import json

from app.models.tool_models import CODE_EXECUTION_TOOL
from app.services.ollama_service import OllamaService
from app.tools.tool_registry import TOOL_REGISTRY


def test_code_execution_complete():

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": (
                "Calculate (25 + 15) * 3 "
                "using the calculation tool."
            )
        }
    ]

    response = service.chat_with_tools(
        messages=messages,
        tools=[CODE_EXECUTION_TOOL],
    )

    tool_calls = response["message"].get(
        "tool_calls",
        []
    )

    if not tool_calls:
        print("\nNo tool call generated.")
        return

    messages.append(response["message"])

    for tool_call in tool_calls:

        tool_name = tool_call.function.name
        arguments = tool_call.function.arguments

        print("\nExecuting Tool:")
        print(tool_name)

        print("\nArguments:")
        print(arguments)

        tool_function = TOOL_REGISTRY.get(
            tool_name
        )

        result = tool_function(**arguments)

        print("\nTool Result:")
        print(result)

        messages.append(
            {
                "role": "tool",
                "tool_name": tool_name,
                "content": json.dumps(result),
            }
        )

    final_response = service.chat(messages)

    print("\nFinal Response:")
    print(final_response)


if __name__ == "__main__":
    test_code_execution_complete()