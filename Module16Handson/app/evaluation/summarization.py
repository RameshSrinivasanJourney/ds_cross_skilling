from app.evaluation.faithfulness import (
    FaithfulnessChecker,
)

from app.metrics.text_metrics import (
    rouge_scores,
)


class SummarizationEvaluator:
    """Evaluate generated summaries."""

    def __init__(self) -> None:

        self.faithfulness = (
            FaithfulnessChecker()
        )

    def evaluate(
        self,
        source: str,
        reference_summary: str,
        generated_summary: str,
    ) -> dict:

        rouge1, rouge2, rouge_l = (
            rouge_scores(
                generated_summary,
                reference_summary,
            )
        )

        faithful, faithfulness_score = (
            self.faithfulness.validate(
                source,
                generated_summary,
            )
        )

        return {
            "rouge1": rouge1,
            "rouge2": rouge2,
            "rougeL": rouge_l,
            "faithfulness_score": (
                faithfulness_score
            ),
            "faithful": faithful,
        }