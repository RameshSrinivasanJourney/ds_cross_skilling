import json

from app.models.tool_models import CALENDAR_TOOL
from app.services.ollama_service import OllamaService
from app.tools.tool_registry import TOOL_REGISTRY


def test_calendar_complete():

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": (
                "Schedule a meeting called "
                "'Module 7 Review' on August 20, 2026 "
                "from 10:00 AM to 11:00 AM. "
                "Use the exact time format HH:MM, "
                "so start_time must be '10:00' and "
                "end_time must be '11:00'."
            )
        }
    ]

    response = service.chat_with_tools(
        messages=messages,
        tools=[CALENDAR_TOOL],
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

        if tool_function is None:
            raise ValueError(
                f"Unknown tool: {tool_name}"
            )

        result = tool_function(
            **arguments
        )

        print("\nTool Result:")
        print(result)

        messages.append(
            {
                "role": "tool",
                "tool_name": tool_name,
                "content": json.dumps(result),
            }
        )

        if result.get("status") == "created":

            messages.append(
                {
                    "role": "user",
                    "content": (
                        "The calendar tool returned a successful "
                        "result. Give me a short confirmation. "
                        "Do not generate Python code."
                    ),
                }
            )

        else:

            messages.append(
                {
                    "role": "user",
                    "content": (
                        "The calendar tool returned a failure. "
                        "Explain the failure to the user clearly. "
                        "Do not claim that the event was created. "
                        "Do not generate Python code."
                    ),
                }
            )

        final_response = service.chat(
            messages
        )

        print("\nFinal Response:")
        print(final_response)


if __name__ == "__main__":
    test_calendar_complete()