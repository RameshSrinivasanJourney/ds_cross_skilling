from app.evaluation.faithfulness import (
    FaithfulnessChecker,
)

from app.metrics.text_metrics import (
    exact_match,
)


class QAEvaluator:
    """Evaluate question-answering responses."""

    def __init__(self):

        self.faithfulness = (
            FaithfulnessChecker()
        )

    def evaluate(
        self,
        question: str,
        reference_answer: str,
        generated_answer: str,
        context: str | None = None,
    ) -> dict:

        result = {
            "exact_match": exact_match(
                generated_answer,
                reference_answer,
            ),
        }

        if context:

            faithful, score = (
                self.faithfulness.validate(
                    context,
                    generated_answer,
                )
            )

            result["groundedness_score"] = (
                score
            )

            result["grounded"] = (
                faithful
            )

        return result