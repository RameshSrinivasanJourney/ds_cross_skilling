from app.models.tool_models import EMAIL_TOOL
from app.services.ollama_service import OllamaService


def test_email_tool_calling():

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": (
                "Send an email to "
                "ramesh@example.com "
                "with subject 'Module 7 Test' "
                "and body 'Function calling is working.'"
            )
        }
    ]

    response = service.chat_with_tools(
        messages=messages,
        tools=[EMAIL_TOOL],
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
    test_email_tool_calling()