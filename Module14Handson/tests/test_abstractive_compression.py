from app.compression.abstractive import (
    AbstractiveCompressor,
)
from app.compression.metrics import (
    calculate_metrics,
)


TEXT = """
Retrieval-Augmented Generation, commonly
called RAG, combines retrieval and generation.
A retrieval system searches a knowledge source
for information relevant to the user's question.
That retrieved context is then given to the
language model so the model can generate an
answer grounded in the retrieved information.
RAG is useful when enterprise information changes
frequently because the retrieval source can be
updated without retraining the model. It can
also reduce unsupported answers by providing
relevant source information.
""".strip()


def test_abstractive():

    question = (
        "What is RAG and why is it useful?"
    )

    compressor = (
        AbstractiveCompressor()
    )

    compressed = compressor.compress(
        TEXT,
        question,
    )

    metrics = calculate_metrics(
        TEXT,
        compressed,
    )

    print(
        "\n=== ORIGINAL ==="
    )
    print(TEXT)

    print(
        "\n=== ABSTRACTIVE ==="
    )
    print(compressed)

    print(
        "\n=== METRICS ==="
    )
    print(metrics)


if __name__ == "__main__":
    test_abstractive()