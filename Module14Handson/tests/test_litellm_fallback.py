from app.routing.fallback_router import (
    FallbackRouter,
)
from app.routing.litellm_service import (
    LiteLLMService,
)


def test_fallback():

    service = LiteLLMService()

    router = FallbackRouter(
        service.generate
    )

    models = [
        "ollama/nonexistent-model",
        "ollama/llama3.2:3b",
    ]

    result = router.run(
        "Explain embeddings.",
        models,
    )

    print(
        "\n=== FALLBACK RESULT ==="
    )

    print(
        result
    )

    assert result["success"] is True

    assert (
        result["model"]
        == "ollama/llama3.2:3b"
    )


if __name__ == "__main__":
    test_fallback()