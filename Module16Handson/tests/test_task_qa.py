from app.evaluation.qa import (
    QAEvaluator,
)


def test_qa():

    evaluator = QAEvaluator()

    question = (
        "What does RAG use to generate an answer?"
    )

    context = (
        "RAG retrieves relevant documents "
        "from a knowledge source and provides "
        "the retrieved context to a language model."
    )

    reference = (
        "RAG uses retrieved context from a "
        "knowledge source to generate an answer."
    )

    generated = (
        "RAG uses retrieved context from a "
        "knowledge source to generate an answer."
    )

    result = evaluator.evaluate(
        question,
        reference,
        generated,
        context,
    )

    print(
        "\n=== QA EVALUATION ==="
    )

    print(result)


if __name__ == "__main__":
    test_qa()