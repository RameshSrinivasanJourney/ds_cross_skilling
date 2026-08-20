import json

from app.models.tool_models import WEB_SCRAPER_TOOL
from app.services.ollama_service import OllamaService
from app.tools.tool_registry import TOOL_REGISTRY


def test_web_scraper_complete():

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

    messages.append(
        {
            "role": "user",
            "content": (
                "Based on the webpage content returned "
                "by the tool, explain in one or two "
                "sentences what this webpage is about. "
                "Do not generate code."
            )
        }
    )

    final_response = service.chat(
        messages
    )

    print("\nFinal Response:")
    print(final_response)


if __name__ == "__main__":
    test_web_scraper_complete()