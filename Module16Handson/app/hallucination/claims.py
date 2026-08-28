import re
from dataclasses import dataclass
from app.hallucination.entailment import (
    EntailmentChecker,
)

@dataclass(frozen=True)
class ClaimResult:
    claim: str
    supported: bool
    score: float


class ClaimExtractor:

    @staticmethod
    def extract(
        text: str,
    ) -> list[str]:

        sentences = re.split(
            r"(?<=[.!?])\s+",
            text.strip(),
        )

        return [
            sentence.strip()
            for sentence in sentences
            if sentence.strip()
        ]

class FactScoreEvaluator:

    def __init__(self):

        self.claim_extractor = (
            ClaimExtractor()
        )

        self.entailment = (
            EntailmentChecker()
        )

    def evaluate(
        self,
        context: str,
        answer: str,
    ) -> dict:

        claims = (
            self.claim_extractor.extract(
                answer
            )
        )

        results = []

        for claim in claims:

            result = self.entailment.check(
                context,
                claim,
            )

            results.append(
                ClaimResult(
                    claim=claim,
                    supported=(
                        result.supported
                    ),
                    score=result.score,
                )
            )

        if not results:

            fact_score = 0.0

        else:

            fact_score = (
                sum(
                    result.supported
                    for result in results
                )
                / len(results)
            )

        return {
            "fact_score": fact_score,
            "claims": results,
        }