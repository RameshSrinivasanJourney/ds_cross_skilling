from app.models.tool_models import READ_FILE_TOOL
from app.services.ollama_service import OllamaService


def test_file_tool_calling():

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": (
                "Read the contents of sample.txt."
            )
        }
    ]

    response = service.chat_with_tools(
        messages=messages,
        tools=[READ_FILE_TOOL],
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
    test_file_tool_calling()