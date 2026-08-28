from app.evaluation.summarization import (
    SummarizationEvaluator,
)


def test_summarization():

    source = (
        "Retrieval-Augmented Generation combines "
        "information retrieval with language model "
        "generation. A retrieval system searches a "
        "knowledge base for relevant documents. "
        "The retrieved context is given to the "
        "language model, which generates an answer. "
        "RAG is useful when information changes "
        "frequently because the knowledge source "
        "can be updated independently."
    )

    reference = (
        "RAG retrieves relevant documents and "
        "provides them to a language model to "
        "generate an answer."
    )

    generated = (
        "RAG retrieves relevant documents and "
        "provides the context to a language model "
        "for answer generation."
    )

    evaluator = (
        SummarizationEvaluator()
    )

    result = evaluator.evaluate(
        source,
        reference,
        generated,
    )

    print(
        "\n=== SUMMARIZATION EVALUATION ==="
    )

    print(result)


if __name__ == "__main__":
    test_summarization()