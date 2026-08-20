from app.models.tool_models import (
    CURRENT_WEATHER_TOOL,
    CALCULATOR_TOOL_MULTI_TURN,
)
from app.services.ollama_service import OllamaService
from app.services.tool_executor import ToolExecutor
from app.tools.tool_registry import TOOL_REGISTRY


def test_parallel_execution():

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

    executor = ToolExecutor(TOOL_REGISTRY)

    print("\nExecuting tools concurrently...")

    results = executor.execute_parallel(
        tool_calls
    )

    print("\nParallel Tool Results:")

    for result in results:
        print(result)


if __name__ == "__main__":
    test_parallel_execution()