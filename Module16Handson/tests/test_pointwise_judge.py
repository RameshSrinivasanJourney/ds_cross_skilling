from app.judges.llm_judge import (
    LLMJudge,
)


def test_pointwise_judge():

    judge = LLMJudge()

    question = (
        "What is Retrieval-Augmented Generation?"
    )

    answer = (
        "RAG retrieves relevant information "
        "from a knowledge source and provides "
        "that context to a language model to "
        "generate an answer."
    )

    reference = (
        "RAG retrieves relevant information "
        "and provides the retrieved context "
        "to a language model for generation."
    )

    result = judge.pointwise(
        question=question,
        answer=answer,
        reference=reference,
    )

    print(
        "\n=== POINTWISE JUDGMENT ==="
    )

    print(
        f"Question: {question}"
    )

    print(
        f"Answer: {answer}"
    )

    print(
        f"Judge result: {result}"
    )


if __name__ == "__main__":
    test_pointwise_judge()