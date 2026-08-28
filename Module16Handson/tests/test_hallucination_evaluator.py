from app.hallucination.evaluator import (
    HallucinationEvaluator,
)


def test_hallucination_evaluator():

    context = (
        "RAG retrieves relevant documents "
        "from a knowledge base and provides "
        "the retrieved context to a language "
        "model for answer generation."
    )

    answer = (
        "RAG retrieves relevant documents "
        "and provides context to a language model. "
        "RAG completely eliminates hallucinations."
    )

    evaluator = (
        HallucinationEvaluator()
    )

    result = evaluator.evaluate(
        context,
        answer,
    )

    print(
        "\n=== HALLUCINATION EVALUATION ==="
    )

    print(
        f"Answer supported: "
        f"{result['answer_supported']}"
    )

    print(
        f"Answer support score: "
        f"{result['answer_support_score']:.4f}"
    )

    print(
        f"Fact score: "
        f"{result['fact_score']:.4f}"
    )

    for claim in result["claims"]:

        print(
            "\nClaim:"
        )

        print(
            claim["claim"]
        )

        print(
            f"Supported: "
            f"{claim['supported']}"
        )

        print(
            f"Score: "
            f"{claim['score']:.4f}"
        )


if __name__ == "__main__":
    test_hallucination_evaluator()