from app.evaluation.golden_runner import (
    GoldenDatasetRunner,
)


def test_golden_runner():

    predictions = {
        "qa-001": (
            "RAG retrieves relevant information "
            "and provides that context to a "
            "language model to generate an answer."
        ),

        "qa-002": (
            "An embedding is a numerical vector "
            "representation of data that captures "
            "semantic relationships."
        ),

        "qa-003": (
            "A vector database stores vector "
            "embeddings and searches for "
            "semantically similar data."
        ),

        "qa-004": (
            "Prompt injection is an attack where "
            "untrusted input attempts to manipulate "
            "the instructions followed by an AI system."
        ),

        "qa-005": (
            "Caching stores reusable results so "
            "repeated requests can avoid unnecessary "
            "model calls and reduce latency and cost."
        ),
    }

    runner = GoldenDatasetRunner()

    result = runner.evaluate(
        predictions
    )

    print(
        "\n=== GOLDEN DATASET RUN ==="
    )

    print(
        f"Exact Match: "
        f"{result['exact_match']:.4f}"
    )

    print(
        f"ROUGE-L: "
        f"{result['rouge_l']:.4f}"
    )

    print(
        f"Faithfulness: "
        f"{result['faithfulness']:.4f}"
    )

    for detail in result[
        "details"
    ]:

        print(
            f"\n{detail['id']}"
        )

        print(
            detail
        )


if __name__ == "__main__":
    test_golden_runner()