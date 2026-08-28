from bert_score import score


def test_bertscore():

    reference = (
        "RAG retrieves relevant information "
        "and uses it to generate an answer."
    )

    prediction = (
        "Retrieval-Augmented Generation "
        "finds useful context and uses it "
        "to produce a response."
    )

    precision, recall, f1 = score(
        [prediction],
        [reference],
        lang="en",
    )

    print(
        "\n=== BERTSCORE ==="
    )

    print(
        f"Precision: "
        f"{precision.item():.4f}"
    )

    print(
        f"Recall: "
        f"{recall.item():.4f}"
    )

    print(
        f"F1: "
        f"{f1.item():.4f}"
    )


if __name__ == "__main__":
    test_bertscore()