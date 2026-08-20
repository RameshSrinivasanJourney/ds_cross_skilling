from app.models.tool_models import WEB_SCRAPER_TOOL
from app.services.ollama_service import OllamaService


def test_web_scraper_tool_calling():

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": (
                "Read the webpage "
                "https://example.com and tell me "
                "what it is about."
            )
        }
    ]

    response = service.chat_with_tools(
        messages=messages,
        tools=[WEB_SCRAPER_TOOL],
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
    test_web_scraper_tool_calling()