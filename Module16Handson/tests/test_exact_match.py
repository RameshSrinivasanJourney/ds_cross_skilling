from app.metrics.text_metrics import (
    exact_match,
)


def test_exact_match():

    reference = (
        "RAG retrieves relevant information."
    )

    same = (
        "RAG retrieves relevant information."
    )

    case_difference = (
        "  rag retrieves relevant information.  "
    )

    different = (
        "RAG generates text."
    )

    print(
        "\n=== EXACT MATCH ==="
    )

    print(
        f"Same: "
        f"{exact_match(same, reference)}"
    )

    print(
        f"Case/whitespace difference: "
        f"{exact_match(case_difference, reference)}"
    )

    print(
        f"Different: "
        f"{exact_match(different, reference)}"
    )

    assert exact_match(
        same,
        reference,
    ) == 1.0

    assert exact_match(
        case_difference,
        reference,
    ) == 1.0

    assert exact_match(
        different,
        reference,
    ) == 0.0


if __name__ == "__main__":
    test_exact_match()