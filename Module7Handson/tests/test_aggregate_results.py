import json

from app.models.tool_models import (
    CURRENT_WEATHER_TOOL,
    CALCULATOR_TOOL_MULTI_TURN,
)
from app.services.ollama_service import OllamaService
from app.services.tool_executor import ToolExecutor
from app.tools.tool_registry import TOOL_REGISTRY


def test_aggregate_results():

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

    # First LLM call
    response = service.chat_with_tools(
        messages=messages,
        tools=[
            CURRENT_WEATHER_TOOL,
            CALCULATOR_TOOL_MULTI_TURN,
        ],
    )

    tool_calls = response["message"].get(
        "tool_calls",
        []
    )

    print("\nNumber of Tool Calls:")
    print(len(tool_calls))

    if not tool_calls:
        print("\nNo tool calls generated.")
        return

    # Add assistant tool-call message
    messages.append(response["message"])

    # Execute all tools concurrently
    executor = ToolExecutor(TOOL_REGISTRY)

    print("\nExecuting tools concurrently...")

    results = executor.execute_parallel(
        tool_calls
    )

    print("\nAggregated Results:")

    for result in results:
        print(result)

    # Add each tool result to conversation
    for result in results:

        messages.append(
            {
                "role": "tool",
                "tool_name": result["tool_name"],
                "content": json.dumps(
                    result["result"]
                ),
            }
        )

    print("\nMessages sent back to Ollama:")

    for message in messages:
        print(message)

    # Second LLM call
    final_response = service.chat(messages)

    print("\nFinal Response:")
    print(final_response)


if __name__ == "__main__":
    test_aggregate_results()