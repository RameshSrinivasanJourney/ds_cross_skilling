from app.evaluation.dialogue import (
    DialogueEvaluator,
)


def test_dialogue():

    conversation = [
        {
            "role": "user",
            "content": (
                "I need help understanding RAG."
            ),
        },
        {
            "role": "assistant",
            "content": (
                "Sure. What would you like to know?"
            ),
        },
        {
            "role": "user",
            "content": (
                "Explain retrieval and generation."
            ),
        },
    ]

    response = (
        "RAG retrieves relevant information "
        "and gives it to a language model for "
        "generation."
    )

    evaluator = (
        DialogueEvaluator()
    )

    result = evaluator.evaluate(
        conversation,
        response,
        required_terms=[
            "retrieves",
            "language model",
            "generation",
        ],
    )

    print(
        "\n=== DIALOGUE EVALUATION ==="
    )

    print(result)


if __name__ == "__main__":
    test_dialogue()