import json

from app.models.tool_models import (
    CURRENT_WEATHER_TOOL,
    CALCULATOR_TOOL_MULTI_TURN,
)

from app.services.ollama_service import OllamaService
from app.tools.tool_registry import TOOL_REGISTRY


def test_tool_chaining():

    service = OllamaService()

    tools = [
        CURRENT_WEATHER_TOOL,
        CALCULATOR_TOOL_MULTI_TURN,
    ]

    messages = [
        {
            "role": "user",
            "content": (
                "What is the current temperature "
                "in Chennai? Then multiply the "
                "temperature by 2."
            )
        }
    ]

    # -------------------------------------------------
    # Step 1: Ask LLM which tool should be used
    # -------------------------------------------------

    response = service.chat_with_tools(
        messages=messages,
        tools=tools,
    )

    tool_calls = response["message"].get(
        "tool_calls",
        []
    )

    if not tool_calls:
        print("\nNo tool call generated.")
        return

    messages.append(response["message"])

    # -------------------------------------------------
    # Step 2: Execute weather tool
    # -------------------------------------------------

    weather_call = tool_calls[0]

    tool_name = weather_call.function.name
    arguments = weather_call.function.arguments

    print("\nExecuting Tool:")
    print(tool_name)

    print("Arguments:")
    print(arguments)

    tool_function = TOOL_REGISTRY.get(
        tool_name
    )

    if tool_function is None:
        raise ValueError(
            f"Unknown tool: {tool_name}"
        )

    weather_result = tool_function(
        **arguments
    )

    print("Tool Result:")
    print(weather_result)

    messages.append(
        {
            "role": "tool",
            "tool_name": tool_name,
            "content": json.dumps(
                weather_result
            ),
        }
    )

    # -------------------------------------------------
    # Step 3: Extract temperature from Tool 1
    # -------------------------------------------------

    temperature = weather_result.get(
        "temperature"
    )

    if temperature is None:
        raise ValueError(
            "Weather tool did not return "
            "a temperature."
        )

    print("\nExtracted Temperature:")
    print(temperature)

    # -------------------------------------------------
    # Step 4: Chain result into Calculator
    # -------------------------------------------------

    calculator_function = TOOL_REGISTRY.get(
        "calculate"
    )

    if calculator_function is None:
        raise ValueError(
            "Calculator tool not found."
        )

    calculator_arguments = {
        "a": temperature,
        "b": 2,
        "operation": "multiply",
    }

    print("\nExecuting Tool:")
    print("calculate")

    print("Arguments:")
    print(calculator_arguments)

    calculation_result = calculator_function(
        **calculator_arguments
    )

    print("Tool Result:")
    print(calculation_result)

    messages.append(
        {
            "role": "tool",
            "tool_name": "calculate",
            "content": json.dumps(
                calculation_result
            ),
        }
    )

    # -------------------------------------------------
    # Step 5: Generate final response
    # -------------------------------------------------

    messages.append(
        {
            "role": "user",
            "content": (
                "Using the weather result and "
                "calculation result, provide the "
                "final answer. Do not generate code."
            )
        }
    )

    final_response = service.chat(
        messages
    )

    print("\nFinal Response:")
    print(final_response)


if __name__ == "__main__":
    test_tool_chaining()