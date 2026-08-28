from app.judges.llm_judge import (
    LLMJudge,
)


def test_pairwise_judge():

    judge = LLMJudge()

    question = (
        "What is Retrieval-Augmented Generation?"
    )

    answer_a = (
        "RAG retrieves relevant documents "
        "from a knowledge source and provides "
        "them as context to a language model "
        "to generate a grounded answer."
    )

    answer_b = (
        "RAG is an AI system that uses data "
        "to answer questions."
    )

    result = judge.pairwise(
        question=question,
        answer_a=answer_a,
        answer_b=answer_b,
    )

    print(
        "\n=== PAIRWISE JUDGMENT ==="
    )

    print(
        f"Question: {question}"
    )

    print(
        "\nAnswer A:"
    )

    print(answer_a)

    print(
        "\nAnswer B:"
    )

    print(answer_b)

    print(
        "\nJudge result:"
    )

    print(result)


if __name__ == "__main__":
    test_pairwise_judge()