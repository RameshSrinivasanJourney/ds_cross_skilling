from app.models.tool_models import SEARCH_EMPLOYEES_TOOL
from app.services.ollama_service import OllamaService


def test_array_parameter():

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": (
                "Search for employees with these skills: "
                "Python, SQL, AWS. Location: Chennai."
            )
        }
    ]

    response = service.chat_with_tools(
        messages=messages,
        tools=[SEARCH_EMPLOYEES_TOOL],
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
    test_array_parameter()