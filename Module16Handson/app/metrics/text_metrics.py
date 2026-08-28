from __future__ import annotations

from dataclasses import dataclass

import sacrebleu
from nltk.translate.meteor_score import (
    meteor_score,
)
from rouge_score import (
    rouge_scorer,
)


@dataclass
class TextMetrics:
    exact_match: float
    bleu: float
    rouge1: float
    rouge2: float
    rouge_l: float
    meteor: float


def normalize_text(
    text: str,
) -> str:
    """Normalize text for exact-match comparison."""

    return " ".join(
        text.lower().strip().split()
    )


def exact_match(
    prediction: str,
    reference: str,
) -> float:

    return float(
        normalize_text(
            prediction
        )
        == normalize_text(
            reference
        )
    )


def bleu_score(
    prediction: str,
    reference: str,
) -> float:

    result = sacrebleu.sentence_bleu(
        prediction,
        [reference],
    )

    return result.score


def rouge_scores(
    prediction: str,
    reference: str,
) -> tuple[float, float, float]:

    scorer = rouge_scorer.RougeScorer(
        [
            "rouge1",
            "rouge2",
            "rougeL",
        ],
        use_stemmer=True,
    )

    scores = scorer.score(
        reference,
        prediction,
    )

    return (
        scores["rouge1"].fmeasure,
        scores["rouge2"].fmeasure,
        scores["rougeL"].fmeasure,
    )


def meteor(
    prediction: str,
    reference: str,
) -> float:

    prediction_tokens = (
        prediction.lower().split()
    )

    reference_tokens = (
        reference.lower().split()
    )

    return meteor_score(
        [reference_tokens],
        prediction_tokens,
    )


def calculate_text_metrics(
    prediction: str,
    reference: str,
) -> TextMetrics:

    rouge1, rouge2, rouge_l = (
        rouge_scores(
            prediction,
            reference,
        )
    )

    return TextMetrics(
        exact_match=exact_match(
            prediction,
            reference,
        ),
        bleu=bleu_score(
            prediction,
            reference,
        ),
        rouge1=rouge1,
        rouge2=rouge2,
        rouge_l=rouge_l,
        meteor=meteor(
            prediction,
            reference,
        ),
    )