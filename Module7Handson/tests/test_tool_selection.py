from app.models.tool_models import (
    WEATHER_TOOL,
    CALCULATOR_TOOL,
    WEB_SCRAPER_TOOL,
)

from app.services.ollama_service import OllamaService


def test_tool_selection():

    service = OllamaService()

    tools = [
        WEATHER_TOOL,
        CALCULATOR_TOOL,
        WEB_SCRAPER_TOOL,
    ]

    messages = [
        {
            "role": "user",
            "content": (
                "What is the current weather "
                "in Chennai?"
            )
        }
    ]

    response = service.chat_with_tools(
        messages=messages,
        tools=tools,
    )

    print("\nUser Question:")
    print(messages[0]["content"])

    tool_calls = response["message"].get(
        "tool_calls",
        []
    )

    print("\nSelected Tool:")

    for tool_call in tool_calls:

        print(
            f"Name: "
            f"{tool_call.function.name}"
        )

        print(
            f"Arguments: "
            f"{tool_call.function.arguments}"
        )


if __name__ == "__main__":
    test_tool_selection()