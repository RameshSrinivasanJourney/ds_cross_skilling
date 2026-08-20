from app.models.tool_models import CALCULATOR_TOOL_MULTI_TURN
from app.services.ollama_service import OllamaService
from app.tools.tool_registry import TOOL_REGISTRY


def test_multi_turn_tools():

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": (
                "First calculate 32 multiplied by 2. "
                "Then take that result and add 10. "
                "Give me the final result."
            )
        }
    ]

    response = service.chat_with_multi_turn_tools(
        messages=messages,
        tools=[CALCULATOR_TOOL_MULTI_TURN],
        tool_registry=TOOL_REGISTRY,
    )

    print("\nFinal Response:")
    print(response)


if __name__ == "__main__":
    test_multi_turn_tools()