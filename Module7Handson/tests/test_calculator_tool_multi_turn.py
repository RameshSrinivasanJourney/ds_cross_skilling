from app.models.tool_models import CALCULATOR_TOOL_MULTI_TURN
from app.services.ollama_service import OllamaService


def test_calculator_tool():

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": "Calculate 32 multiplied by 2."
        }
    ]

    response = service.chat_with_tools(
        messages=messages,
        tools=[CALCULATOR_TOOL_MULTI_TURN],
    )

    print("\nUser Question:")
    print(messages[0]["content"])

    tool_calls = response["message"].get("tool_calls", [])

    if not tool_calls:
        print("\nNo tool call generated.")
        return

    for tool_call in tool_calls:
        print("\nTool Call:")
        print(tool_call)


if __name__ == "__main__":
    test_calculator_tool()