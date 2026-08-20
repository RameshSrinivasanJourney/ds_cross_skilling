from app.models.tool_models import CREATE_CUSTOMER_TOOL
from app.services.ollama_service import OllamaService


def test_nested_customer_tool():

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": (
                "Create a customer named Ramesh Srinivasan. "
                "His email is ramesh@example.com. "
                "He lives in Chennai, Tamil Nadu, India."
            )
        }
    ]

    response = service.chat_with_tools(
        messages=messages,
        tools=[CREATE_CUSTOMER_TOOL],
    )

    print("\nUser Question:")
    print(messages[0]["content"])

    print("\nTool Call:")

    tool_calls = response["message"].get("tool_calls", [])

    if tool_calls:
        for tool_call in tool_calls:
            print(tool_call)

            print("\nArguments:")
            print(tool_call.function.arguments)
    else:
        print("No tool call generated.")


if __name__ == "__main__":
    test_nested_customer_tool()