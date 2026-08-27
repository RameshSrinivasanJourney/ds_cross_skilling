from app.validation.faithfulness import (
    FaithfulnessChecker,
)


def test_faithfulness():

    checker = (
        FaithfulnessChecker()
    )

    context = (
        "RAG retrieves relevant documents "
        "from a knowledge source and "
        "provides the retrieved information "
        "to a language model."
    )

    faithful_answer = (
        "RAG retrieves relevant documents "
        "and provides them to a language model."
    )

    unsupported_answer = (
        "RAG guarantees completely accurate "
        "answers and eliminates hallucinations "
        "in every situation."
    )

    good, good_score = (
        checker.validate(
            context,
            faithful_answer,
        )
    )

    bad, bad_score = (
        checker.validate(
            context,
            unsupported_answer,
        )
    )

    print(
        "\nFaithful result:"
    )

    print(
        good,
        good_score,
    )

    print(
        "\nUnsupported result:"
    )

    print(
        bad,
        bad_score,
    )

    assert good is True

    assert bad is False


if __name__ == "__main__":
    test_faithfulness()