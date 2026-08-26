from app.compression.extractive import (
    compress_extractive,
)
from app.compression.metrics import (
    calculate_metrics,
)


TEXT = """
Retrieval-Augmented Generation, or RAG,
combines information retrieval with language
model generation. A retriever searches a
knowledge base for relevant documents. The
retrieved information is then supplied to a
language model. The model uses that context
to produce an answer. RAG is especially useful
when the information changes frequently. It can
also ground answers in private enterprise data.
Large prompts can increase latency and token
usage. Removing redundant context can reduce
the amount of information sent to the model.
""".strip()


def test_extractive():

    question = (
        "How does RAG reduce hallucination "
        "and why is prompt compression useful?"
    )

    compressed = compress_extractive(
        TEXT,
        question,
        keep_ratio=0.5,
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
        "\n=== EXTRACTIVE ==="
    )
    print(compressed)

    print(
        "\n=== METRICS ==="
    )
    print(metrics)


if __name__ == "__main__":
    test_extractive()