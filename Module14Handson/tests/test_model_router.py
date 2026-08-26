from app.routing.cost_aware_router import (
    CostAwareRouter,
)


def test_model_router():

    router = CostAwareRouter(
        cheap_model="ollama/llama3.2:3b",
        powerful_model="ollama/llama3.2:3b",
    )

    prompts = [
        "What is RAG?",
        (
            "Design and compare two "
            "multi-tenant RAG architectures, "
            "including scalability, security, "
            "latency, and trade-offs."
        ),
    ]

    for prompt in prompts:

        decision = router.route(
            prompt
        )

        print(
            "\nPrompt:"
        )
        print(prompt)

        print(
            f"Complexity: "
            f"{decision.complexity}"
        )

        print(
            f"Score: "
            f"{decision.score}"
        )

        print(
            f"Model: "
            f"{decision.model}"
        )

        print(
            f"Reason: "
            f"{decision.reason}"
        )


if __name__ == "__main__":
    test_model_router()