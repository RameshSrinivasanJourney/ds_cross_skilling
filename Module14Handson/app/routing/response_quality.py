from dataclasses import dataclass


@dataclass(frozen=True)
class QualityResult:
    score: float
    accepted: bool
    reasons: list[str]


class ResponseQualityEvaluator:
    """Simple deterministic response quality check."""

    def evaluate(
        self,
        prompt: str,
        response: str,
    ) -> QualityResult:

        score = 1.0
        reasons: list[str] = []

        answer = response.strip()

        if not answer:

            return QualityResult(
                score=0.0,
                accepted=False,
                reasons=[
                    "empty_response"
                ],
            )

        if len(answer) < 30:

            score -= 0.4

            reasons.append(
                "very_short_response"
            )

        failure_phrases = [
            "i don't know",
            "i cannot answer",
            "i can't answer",
            "unable to answer",
            "error",
        ]

        if any(
            phrase in answer.lower()
            for phrase in failure_phrases
        ):

            score -= 0.7

            reasons.append(
                "failure_phrase"
            )

        question_words = set(
            prompt.lower().split()
        )

        answer_words = set(
            answer.lower().split()
        )

        overlap = (
            len(
                question_words
                & answer_words
            )
        )

        if overlap == 0:

            score -= 0.3

            reasons.append(
                "low_topic_overlap"
            )

        score = max(
            0.0,
            min(1.0, score),
        )

        return QualityResult(
            score=score,
            accepted=score >= 0.6,
            reasons=reasons,
        )