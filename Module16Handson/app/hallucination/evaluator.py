from app.hallucination.claims import (
    FactScoreEvaluator,
)

from app.hallucination.entailment import (
    EntailmentChecker,
)


class HallucinationEvaluator:

    def __init__(self):

        self.entailment = (
            EntailmentChecker()
        )

        self.factscore = (
            FactScoreEvaluator()
        )

    def evaluate(
        self,
        context: str,
        answer: str,
    ) -> dict:

        claims = (
            self.factscore.evaluate(
                context,
                answer,
            )
        )

        overall_entailment = (
            self.entailment.check(
                context,
                answer,
            )
        )

        return {
            "answer_supported": (
                overall_entailment.supported
            ),
            "answer_support_score": (
                overall_entailment.score
            ),
            "fact_score": (
                claims["fact_score"]
            ),
            "claims": [
                {
                    "claim": claim.claim,
                    "supported": claim.supported,
                    "score": claim.score,
                }
                for claim
                in claims["claims"]
            ],
        }