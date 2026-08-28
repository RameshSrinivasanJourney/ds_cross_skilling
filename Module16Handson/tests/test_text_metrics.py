from app.metrics.text_metrics import (
    calculate_text_metrics,
)


def test_text_metrics():

    reference = (
        "RAG retrieves relevant information "
        "and provides that context to a "
        "language model."
    )

    prediction = (
        "RAG retrieves useful information "
        "and provides the context to an "
        "LLM."
    )

    metrics = calculate_text_metrics(
        prediction,
        reference,
    )

    print(
        "\n=== TEXT GENERATION METRICS ==="
    )

    print(
        f"Exact Match: "
        f"{metrics.exact_match:.4f}"
    )

    print(
        f"BLEU: "
        f"{metrics.bleu:.4f}"
    )

    print(
        f"ROUGE-1: "
        f"{metrics.rouge1:.4f}"
    )

    print(
        f"ROUGE-2: "
        f"{metrics.rouge2:.4f}"
    )

    print(
        f"ROUGE-L: "
        f"{metrics.rouge_l:.4f}"
    )

    print(
        f"METEOR: "
        f"{metrics.meteor:.4f}"
    )


if __name__ == "__main__":
    test_text_metrics()