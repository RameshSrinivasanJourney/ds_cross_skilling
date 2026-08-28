from app.judges.llm_judge import (
    LLMJudge,
)


def test_position_bias():

    judge = LLMJudge()

    question = (
        "What is an embedding?"
    )

    answer_a = (
        "An embedding is a numerical vector "
        "representation that captures semantic "
        "relationships."
    )

    answer_b = (
        "An embedding is a representation of data "
        "used by machine learning systems."
    )

    first = judge.pairwise(
        question,
        answer_a,
        answer_b,
    )

    second = judge.pairwise(
        question,
        answer_b,
        answer_a,
    )

    print(
        "\n=== POSITION BIAS ==="
    )

    print(
        "A vs B:"
    )

    print(first)

    print(
        "\nB vs A:"
    )

    print(second)

    print(
        "\nInterpretation:"
    )

    print(
        "If the judge changes behavior simply "
        "because answer order changed, position "
        "bias may be present."
    )


if __name__ == "__main__":
    test_position_bias()