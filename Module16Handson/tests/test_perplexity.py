from app.metrics.perplexity import (
    PerplexityCalculator,
)


def test_perplexity():

    calculator = (
        PerplexityCalculator()
    )

    texts = [
        (
            "RAG retrieves relevant information "
            "from a knowledge source."
        ),
        (
            "RAG information knowledge retrieves "
            "from random the a source."
        ),
    ]

    for text in texts:

        value = calculator.calculate(
            text
        )

        print(
            "\nText:"
        )

        print(text)

        print(
            f"Perplexity: "
            f"{value:.4f}"
        )


if __name__ == "__main__":
    test_perplexity()