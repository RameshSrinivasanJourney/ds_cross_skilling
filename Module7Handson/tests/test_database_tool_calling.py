from app.models.tool_models import (
    DATABASE_QUERY_TOOL,
)
from app.services.ollama_service import OllamaService


def test_database_tool_calling():

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": (
                "Find all employees who are "
                "based in Chennai."
            )
        }
    ]

    response = service.chat_with_tools(
        messages=messages,
        tools=[DATABASE_QUERY_TOOL],
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
            f"Name: {tool_call.function.name}"
        )

        print(
            f"Arguments: "
            f"{tool_call.function.arguments}"
        )


if __name__ == "__main__":
    test_database_tool_calling()