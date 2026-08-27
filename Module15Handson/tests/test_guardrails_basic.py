from app.guardrails.basic_guard import (
    answer_guard,
)


def test_basic_guard():

    valid_output = {
        "answer": "RAG retrieves relevant information."
    }

    result = answer_guard.parse(
        llm_output=valid_output
    )

    print(
        "\n=== GUARDRAILS BASIC TEST ==="
    )

    print(
        result
    )


if __name__ == "__main__":
    test_basic_guard()