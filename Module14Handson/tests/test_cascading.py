from app.routing.cascade_router import (
    CascadeRouter,
)
from app.routing.model_generation import (
    generate,
)


def test_cascading():

    router = CascadeRouter(
        generate=generate,
        cheap_model=(
            "ollama/llama3.2:3b"
        ),
        powerful_model=(
            "ollama/llama3.2:3b"
        ),
        quality_threshold=0.6,
    )

    prompts = [
        "What is RAG?",
        (
            "Design a production-grade "
            "multi-tenant GenAI architecture "
            "with caching, observability, "
            "session isolation, fallback "
            "routing, security, and scaling. "
            "Explain the trade-offs."
        ),
    ]

    for prompt in prompts:

        result = router.run(
            prompt
        )

        print(
            "\n================================"
        )

        print(
            "PROMPT"
        )

        print(prompt)

        print(
            "\nSELECTED MODEL:"
        )

        print(
            result["selected_model"]
        )

        print(
            "\nESCALATED:"
        )

        print(
            result["escalated"]
        )

        print(
            "\nATTEMPTS:"
        )

        print(
            result["attempts"]
        )

        print(
            "\nQUALITY:"
        )

        print(
            result["quality"]
        )

        print(
            "\nANSWER:"
        )

        print(
            result["answer"]
        )


if __name__ == "__main__":
    test_cascading()