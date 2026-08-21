from app.orchestration.parallel_research import (
    run_parallel_research,
)


def test_parallel_multi_agent():

    question = (
        "An employee wants to know how to approach "
        "a question about company leave policy."
    )

    results = run_parallel_research(
        question
    )

    print("\n=== Parallel Research Results ===")

    for name, result in results.items():

        print(
            f"\n--- {name.upper()} ---"
        )
        print(result)


if __name__ == "__main__":
    test_parallel_multi_agent()