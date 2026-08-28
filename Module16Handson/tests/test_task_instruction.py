from app.evaluation.instruction_following import (
    InstructionFollowingEvaluator,
)


def test_instruction_following():

    evaluator = (
        InstructionFollowingEvaluator()
    )

    response = """- RAG retrieves relevant information.
- The retrieved context is provided to a language model.
- The model uses that context to generate an answer.
"""

    result = evaluator.evaluate(
        response,
        required_terms=[
            "RAG",
            "language model",
            "generate",
        ],
        max_words=40,
        required_bullets=3,
    )

    print(
        "\n=== INSTRUCTION FOLLOWING ==="
    )

    print(result)

    assert result["passed"] is True


if __name__ == "__main__":
    test_instruction_following()