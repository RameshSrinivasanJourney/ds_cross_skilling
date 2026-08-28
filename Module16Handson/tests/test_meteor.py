from app.metrics.text_metrics import (
    meteor,
)


def test_meteor():

    reference = (
        "The model retrieves relevant documents."
    )

    prediction = (
        "The system retrieves useful documents."
    )

    score = meteor(
        prediction,
        reference,
    )

    print(
        "\n=== METEOR ==="
    )

    print(
        f"METEOR: {score:.4f}"
    )


if __name__ == "__main__":
    test_meteor()