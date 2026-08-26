from app.routing.litellm_service import (
    LiteLLMService,
)


def test_litellm_basic():

    service = LiteLLMService()

    result = service.generate(
        "Explain caching in simple terms."
    )

    print(
        "\n=== LITELLM RESULT ==="
    )

    print(
        f"Model: {result['model']}"
    )

    print(
        f"Input tokens: "
        f"{result['input_tokens']}"
    )

    print(
        f"Output tokens: "
        f"{result['output_tokens']}"
    )

    print(
        f"Answer:\n{result['answer']}"
    )


if __name__ == "__main__":
    test_litellm_basic()