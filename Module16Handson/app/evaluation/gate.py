from app.evaluation.config import (
    DEFAULT_THRESHOLDS,
    DATASET_VERSION,
    MODEL_VERSION,
    PROMPT_VERSION,
)

from app.evaluation.result import (
    EvaluationReport,
    EvaluationResult,
)


class EvaluationGate:
    """Apply production-style evaluation thresholds."""

    def __init__(
        self,
        thresholds=DEFAULT_THRESHOLDS,
    ) -> None:

        self.thresholds = thresholds

    def evaluate(
        self,
        *,
        exact_match: float,
        rouge_l: float,
        faithfulness: float,
        judge_score: float,
        hallucination_rate: float,
    ) -> EvaluationReport:

        results = [
            EvaluationResult(
                metric="exact_match",
                value=exact_match,
                threshold=(
                    self.thresholds.min_exact_match
                ),
                passed=(
                    exact_match
                    >= self.thresholds.min_exact_match
                ),
            ),
            EvaluationResult(
                metric="rouge_l",
                value=rouge_l,
                threshold=(
                    self.thresholds.min_rouge_l
                ),
                passed=(
                    rouge_l
                    >= self.thresholds.min_rouge_l
                ),
            ),
            EvaluationResult(
                metric="faithfulness",
                value=faithfulness,
                threshold=(
                    self.thresholds.min_faithfulness
                ),
                passed=(
                    faithfulness
                    >= self.thresholds.min_faithfulness
                ),
            ),
            EvaluationResult(
                metric="judge_score",
                value=judge_score,
                threshold=(
                    self.thresholds.min_judge_score
                ),
                passed=(
                    judge_score
                    >= self.thresholds.min_judge_score
                ),
            ),
            EvaluationResult(
                metric="hallucination_rate",
                value=hallucination_rate,
                threshold=(
                    self.thresholds.max_hallucination_rate
                ),
                passed=(
                    hallucination_rate
                    <= self.thresholds.max_hallucination_rate
                ),
            ),
        ]

        return EvaluationReport(
            prompt_version=PROMPT_VERSION,
            model_version=MODEL_VERSION,
            dataset_version=DATASET_VERSION,
            results=results,
        )