from app.routing.complexity_classifier import (
    ComplexityClassifier,
)


def test_classifier():

    classifier = (
        ComplexityClassifier()
    )

    prompts = [
        "What is RAG?",
        "Explain embeddings in simple terms.",
        (
            "Compare RAG and fine-tuning "
            "and explain the architectural "
            "trade-offs for a multi-tenant "
            "healthcare application."
        ),
    ]

    for prompt in prompts:

        result = classifier.classify(
            prompt
        )

        print(
            "\nPrompt:"
        )
        print(prompt)

        print(
            f"Score: {result.score}"
        )

        print(
            f"Level: {result.level}"
        )

        print(
            f"Reasons: {result.reasons}"
        )


if __name__ == "__main__":
    test_classifier()