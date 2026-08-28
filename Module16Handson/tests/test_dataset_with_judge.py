from app.datasets.dataset_loader import (
    load_json_dataset,
)

from app.judges.llm_judge import (
    LLMJudge,
)


def test_dataset_with_judge():

    dataset = load_json_dataset(
        "data/golden/qa_golden.json"
    )

    judge = LLMJudge()

    scores = []

    for item in dataset:

        result = judge.pointwise(
            question=item["question"],
            answer=item["expected_answer"],
            reference=item["expected_answer"],
        )

        print(
            "\n================================"
        )

        print(
            f"ID: {item['id']}"
        )

        print(
            f"Score: "
            f"{result.get('score')}"
        )

        print(
            f"Reason: "
            f"{result.get('reason')}"
        )

        score = result.get(
            "score"
        )

        if isinstance(
            score,
            (int, float),
        ):

            scores.append(
                float(score)
            )

    if scores:

        average = (
            sum(scores)
            / len(scores)
        )

        print(
            "\n=== AVERAGE JUDGE SCORE ==="
        )

        print(
            f"{average:.2f}"
        )


if __name__ == "__main__":
    test_dataset_with_judge()