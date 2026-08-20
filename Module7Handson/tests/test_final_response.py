from app.models.tool_models import CURRENT_WEATHER_TOOL
from app.services.ollama_service import OllamaService
from app.tools.tool_registry import TOOL_REGISTRY


def test_final_response():

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": "What is the weather in Chennai right now?"
        }
    ]

    response = service.chat_with_tool_execution(
        messages=messages,
        tools=[CURRENT_WEATHER_TOOL],
        tool_registry=TOOL_REGISTRY,
    )

    print("\nFinal Response:")
    print(response)


if __name__ == "__main__":
    test_final_response()