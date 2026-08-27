from app.services.output_validated_llm import (
    OutputValidatedLLM,
)


def test_output_validated_llm():

    service = (
        OutputValidatedLLM()
    )

    context = (
        "RAG retrieves relevant documents "
        "from a knowledge source and gives "
        "the retrieved information to a "
        "language model for generation."
    )

    print(
        "\n=== TEXT OUTPUT ==="
    )

    text_result = (
        service.generate_text(
            "Explain RAG using the provided context.",
            context=context,
        )
    )

    print(
        text_result
    )

    print(
        "\n=== JSON OUTPUT ==="
    )

    json_result = (
        service.generate_json(
            """
Return JSON with exactly these fields:
answer: string
confidence: number between 0 and 1
sources: array of strings

Question:
What is RAG?
""".strip()
        )
    )

    print(
        json_result
    )


if __name__ == "__main__":
    test_output_validated_llm()