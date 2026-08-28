from app.hallucination.polling import (
    PollingEvaluator,
)


def test_chainpoll_style():

    context = (
        "RAG retrieves relevant documents "
        "and gives the retrieved context to "
        "a language model for generation."
    )

    supported_answer = (
        "RAG retrieves documents and supplies "
        "their context to a language model."
    )

    evaluator = (
        PollingEvaluator()
    )

    result = evaluator.evaluate(
        context,
        supported_answer,
        polls=5,
    )

    print(
        "\n=== CHAINPOLL-STYLE TEST ==="
    )

    print(
        f"Votes: {result['votes']}"
    )

    print(
        f"Counts: {result['counts']}"
    )

    print(
        f"Decision: "
        f"{result['decision']}"
    )

    print(
        f"Agreement: "
        f"{result['agreement']:.2%}"
    )


if __name__ == "__main__":
    test_chainpoll_style()