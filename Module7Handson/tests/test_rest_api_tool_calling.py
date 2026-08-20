from app.models.tool_models import REST_API_TOOL
from app.services.ollama_service import OllamaService


def test_rest_api_tool_calling():

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": (
                "Get the list of users from "
                "the REST API."
            )
        }
    ]

    response = service.chat_with_tools(
        messages=messages,
        tools=[REST_API_TOOL],
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
    test_rest_api_tool_calling()