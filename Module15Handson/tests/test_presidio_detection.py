from app.pii.presidio_detector import (
    PIIDetector,
)


def test_presidio_detection():

    detector = PIIDetector()

    text = (
        "My name is Ramesh Srinivasan. "
        "My email is ramesh@example.com "
        "and my phone is +1-212-555-1234."
    )

    results = detector.analyze(
        text
    )

    print(
        "\n=== PII DETECTION ==="
    )

    print(
        f"Input:\n{text}"
    )

    for result in results:

        print(
            f"\nEntity: {result.entity_type}"
        )

        print(
            f"Score: {result.score:.3f}"
        )

        print(
            f"Start: {result.start}"
        )

        print(
            f"End: {result.end}"
        )

        print(
            f"Value: "
            f"{text[result.start:result.end]}"
        )


if __name__ == "__main__":
    test_presidio_detection()