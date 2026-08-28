from app.hallucination.entailment import (
    EntailmentChecker,
)


def test_entailment():

    checker = EntailmentChecker()

    context = (
        "RAG retrieves relevant documents "
        "from a knowledge source and provides "
        "the retrieved context to a language model."
    )

    supported_claim = (
        "RAG retrieves relevant documents "
        "and provides context to a language model."
    )

    unsupported_claim = (
        "RAG guarantees completely accurate "
        "answers in every situation."
    )

    supported = checker.check(
        context,
        supported_claim,
    )

    unsupported = checker.check(
        context,
        unsupported_claim,
    )

    print(
        "\n=== ENTAILMENT CHECK ==="
    )

    print(
        f"Supported claim: {supported}"
    )

    print(
        f"Unsupported claim: {unsupported}"
    )

    assert supported.supported is True

    assert unsupported.supported is False


if __name__ == "__main__":
    test_entailment()