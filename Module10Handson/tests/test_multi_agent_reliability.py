import logging

from app.reliability.reliable_multi_agent import (
    run_reliable_multi_agent,
)


def test_multi_agent_reliability():

    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(message)s"
        ),
    )

    question = (
        "Prepare a concise employee-facing "
        "explanation of how to approach a "
        "company leave-policy question."
    )

    result = run_reliable_multi_agent(
        question
    )

    print("\n=== FINAL RESULT ===")

    print("\nResearch:")
    print(result["research"])

    print("\nDraft:")
    print(result["draft"])


if __name__ == "__main__":
    test_multi_agent_reliability()