from app.models.tool_models import WEB_SEARCH_TOOL
from app.services.ollama_service import OllamaService


def test_web_search_tool_calling():

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": (
                "Search the web and tell me "
                "what the latest Python version is."
            )
        }
    ]

    response = service.chat_with_tools(
        messages=messages,
        tools=[WEB_SEARCH_TOOL],
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
        print(f"Name: {tool_call.function.name}")
        print(f"Arguments: {tool_call.function.arguments}")


if __name__ == "__main__":
    test_web_search_tool_calling()