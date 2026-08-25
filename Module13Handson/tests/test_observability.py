from app.observability.observable_llm import (
    ObservableLLM,
)


def test_observable_llm():

    service = ObservableLLM()

    print(
        "\n=== GENERATION TEST ==="
    )

    answer, observation = (
        service.generate(
            "Explain RAG in simple terms.",
            user_id="employee-001",
            feature="rag-explanation",
        )
    )

    print(
        "\nAnswer:"
    )
    print(answer)

    print(
        "\nObservation:"
    )

    for key, value in (
        observation.to_dict().items()
    ):

        print(
            f"{key}: {value}"
        )

    print(
        "\n=== STREAMING TEST ==="
    )

    stream, metadata = (
        service.stream(
            "Explain embeddings in simple terms.",
            user_id="employee-001",
            feature="embedding-explanation",
        )
    )

    print(
        "\nStreamed Answer:"
    )

    for chunk in stream:
        print(
            chunk,
            end="",
            flush=True,
        )

    print(
        "\n\nStream Metadata:"
    )

    print(metadata)


if __name__ == "__main__":
    test_observable_llm()