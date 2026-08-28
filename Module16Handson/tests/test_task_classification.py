from app.evaluation.classification import (
    ClassificationEvaluator,
)


def test_classification():

    actual = [
        "billing",
        "technical",
        "billing",
        "account",
        "technical",
        "billing",
    ]

    predicted = [
        "billing",
        "technical",
        "technical",
        "account",
        "technical",
        "billing",
    ]

    evaluator = (
        ClassificationEvaluator()
    )

    result = evaluator.evaluate(
        actual,
        predicted,
    )

    print(
        "\n=== CLASSIFICATION EVALUATION ==="
    )

    print(
        result
    )


if __name__ == "__main__":
    test_classification()