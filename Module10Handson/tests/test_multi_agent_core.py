from app.orchestration.multi_agent_system import (
    run_multi_agent_system,
)


def test_multi_agent_core():

    question = (
        "An employee wants to know how to approach "
        "a question about company leave policy."
    )

    result = run_multi_agent_system(
        question
    )

    print("\n=== FINAL RESULT ===")

    print(
        "\nResearch:"
    )
    print(result["research"])

    print(
        "\nAnalysis:"
    )
    print(result["analysis"])

    print(
        "\nDraft:"
    )
    print(result["draft"])

    print(
        "\nReview:"
    )
    print(result["review"])


if __name__ == "__main__":
    test_multi_agent_core()