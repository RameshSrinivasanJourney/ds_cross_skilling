from dataclasses import dataclass


@dataclass(frozen=True)
class EvaluationThresholds:
    min_exact_match: float = 0.60
    min_rouge_l: float = 0.50
    min_faithfulness: float = 0.60
    min_judge_score: float = 3.50
    max_hallucination_rate: float = 0.20


DEFAULT_THRESHOLDS = (
    EvaluationThresholds()
)


PROMPT_VERSION = "v1.0"
MODEL_VERSION = "llama3.2:3b"
DATASET_VERSION = "v1.0"