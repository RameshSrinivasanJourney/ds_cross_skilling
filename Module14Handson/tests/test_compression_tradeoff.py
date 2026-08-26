from app.compression.extractive import (
    compress_extractive,
)
from app.compression.metrics import (
    calculate_metrics,
)
from app.compression.quality import (
    keyword_quality,
)


TEXT = """
Retrieval-Augmented Generation, or RAG,
combines information retrieval with language
model generation. A retriever searches a
knowledge base for relevant documents. The
retrieved documents are supplied to the language
model as context. The model then generates an
answer grounded in that context. RAG is useful
for frequently changing information because the
knowledge source can be updated independently
of the language model. It is also useful for
private enterprise information. Good retrieval
quality is important because irrelevant documents
can lead to poor answers. Long contexts increase
token usage, latency, and sometimes cost.
Prompt compression can remove redundant context
while attempting to preserve important facts.
""".strip()


QUESTION = (
    "Why is RAG useful for changing enterprise "
    "information and what are the benefits of "
    "prompt compression?"
)


REQUIRED_TERMS = [
    "RAG",
    "retrieval",
    "enterprise",
    "changing",
    "compression",
    "token",
]


def test_tradeoff():

    ratios = [
        0.9,
        0.7,
        0.5,
        0.3,
    ]

    print(
        "\n=== COMPRESSION TRADE-OFF ==="
    )

    for ratio in ratios:

        compressed = (
            compress_extractive(
                TEXT,
                QUESTION,
                keep_ratio=ratio,
            )
        )

        metrics = calculate_metrics(
            TEXT,
            compressed,
        )

        quality = keyword_quality(
            compressed,
            REQUIRED_TERMS,
        )

        print(
            f"\nKeep ratio: {ratio}"
        )

        print(
            f"Compression ratio: "
            f"{metrics.compression_ratio:.2f}x"
        )

        print(
            f"Reduction: "
            f"{metrics.reduction_percent:.1f}%"
        )

        print(
            f"Quality score: "
            f"{quality:.2f}"
        )

        print(
            f"Compressed text:\n"
            f"{compressed}"
        )


if __name__ == "__main__":
    test_tradeoff()