from app.hallucination.claims import (
    FactScoreEvaluator,
)


def test_factscore_style():

    context = (
        "RAG retrieves relevant documents "
        "from a knowledge base. The retrieved "
        "context is supplied to a language model "
        "to generate an answer. RAG can be useful "
        "when the knowledge source changes "
        "frequently."
    )

    answer = (
        "RAG retrieves relevant documents "
        "from a knowledge base. The retrieved "
        "context is supplied to a language model. "
        "RAG guarantees that hallucinations "
        "never occur."
    )

    evaluator = (
        FactScoreEvaluator()
    )

    result = evaluator.evaluate(
        context,
        answer,
    )

    print(
        "\n=== FACTSCORE-STYLE TEST ==="
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
            claim.claim
        )

        print(
            f"Supported: "
            f"{claim.supported}"
        )

        print(
            f"Score: "
            f"{claim.score:.4f}"
        )


if __name__ == "__main__":
    test_factscore_style()