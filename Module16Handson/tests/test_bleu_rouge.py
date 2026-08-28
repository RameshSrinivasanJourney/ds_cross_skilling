from app.metrics.text_metrics import (
    bleu_score,
    rouge_scores,
)


def test_bleu_rouge():

    reference = (
        "RAG retrieves relevant information "
        "and provides it to a language model."
    )

    prediction = (
        "RAG retrieves relevant information "
        "and provides the context to a language model."
    )

    bleu = bleu_score(
        prediction,
        reference,
    )

    rouge1, rouge2, rouge_l = (
        rouge_scores(
            prediction,
            reference,
        )
    )

    print(
        "\n=== BLEU / ROUGE ==="
    )

    print(
        f"BLEU: {bleu:.4f}"
    )

    print(
        f"ROUGE-1: {rouge1:.4f}"
    )

    print(
        f"ROUGE-2: {rouge2:.4f}"
    )

    print(
        f"ROUGE-L: {rouge_l:.4f}"
    )


if __name__ == "__main__":
    test_bleu_rouge()