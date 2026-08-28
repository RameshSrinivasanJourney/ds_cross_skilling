from app.datasets.dataset_loader import (
    load_json_dataset,
)

from app.evaluation.faithfulness import (
    FaithfulnessChecker,
)

from app.metrics.text_metrics import (
    exact_match,
    rouge_scores,
)


class GoldenDatasetRunner:

    def __init__(self):

        self.faithfulness = (
            FaithfulnessChecker()
        )

    def evaluate(
        self,
        predictions: dict[str, str],
    ) -> dict:

        dataset = load_json_dataset(
            "data/golden/qa_golden.json"
        )

        exact_scores = []
        rouge_l_scores = []
        faithfulness_scores = []

        details = []

        for item in dataset:

            item_id = item["id"]

            prediction = predictions.get(
                item_id,
                "",
            )

            reference = item[
                "expected_answer"
            ]

            exact = exact_match(
                prediction,
                reference,
            )

            _, _, rouge_l = rouge_scores(
                prediction,
                reference,
            )

            faithfulness = (
                self.faithfulness.score(
                    reference,
                    prediction,
                )
            )

            exact_scores.append(
                exact
            )

            rouge_l_scores.append(
                rouge_l
            )

            faithfulness_scores.append(
                faithfulness
            )

            details.append(
                {
                    "id": item_id,
                    "exact_match": exact,
                    "rouge_l": rouge_l,
                    "faithfulness": faithfulness,
                }
            )

        count = len(dataset)

        return {
            "exact_match": (
                sum(exact_scores)
                / count
            ),
            "rouge_l": (
                sum(rouge_l_scores)
                / count
            ),
            "faithfulness": (
                sum(faithfulness_scores)
                / count
            ),
            "details": details,
        }