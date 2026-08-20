from app.models.tool_models import CALCULATOR_TOOL
from app.services.ollama_service import OllamaService


def test_calculator_enum():

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": "Calculate 25 modulo 4."
        }
    ]

    response = service.chat_with_tools(
        messages=messages,
        tools=[CALCULATOR_TOOL],
    )

    print("\nUser Question:")
    print(messages[0]["content"])

    print("\nTool Call:")

    tool_calls = response["message"].get("tool_calls", [])

    if tool_calls:
        for tool_call in tool_calls:
            print(tool_call)
    else:
        print("No tool call generated.")


if __name__ == "__main__":
    test_calculator_enum()