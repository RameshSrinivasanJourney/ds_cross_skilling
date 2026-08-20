from app.models.tool_models import CALENDAR_TOOL
from app.services.ollama_service import OllamaService


def test_calendar_tool_calling():

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": (
                "Schedule a meeting called "
                "'Module 7 Review' on August 20, 2026 "
                "from 10:00 to 11:00. "
                "The meeting is to review Function "
                "Calling and Tool Use."
            )
        }
    ]

    response = service.chat_with_tools(
        messages=messages,
        tools=[CALENDAR_TOOL],
    )

    print("\nUser Question:")
    print(messages[0]["content"])

    tool_calls = response["message"].get(
        "tool_calls",
        []
    )

    if not tool_calls:
        print("\nNo tool call generated.")
        return

    for tool_call in tool_calls:

        print("\nTool Call:")

        print(
            f"Name: "
            f"{tool_call.function.name}"
        )

        print(
            f"Arguments: "
            f"{tool_call.function.arguments}"
        )


if __name__ == "__main__":
    test_calendar_tool_calling()