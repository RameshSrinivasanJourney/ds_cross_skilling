import re
from dataclasses import dataclass


@dataclass(frozen=True)
class EntailmentResult:
    supported: bool
    score: float


class EntailmentChecker:
    """
    Lightweight educational entailment checker.

    This is a lexical baseline, not a production
    natural-language-inference model.
    """

    STOP_WORDS = {
        "the",
        "a",
        "an",
        "is",
        "are",
        "was",
        "were",
        "to",
        "of",
        "in",
        "on",
        "for",
        "and",
        "or",
        "with",
        "that",
        "this",
        "it",
        "can",
        "be",
        "from",
        "as",
        "by",
    }

    @classmethod
    def words(
        cls,
        text: str,
    ) -> set[str]:

        tokens = re.findall(
            r"\b[a-zA-Z0-9]+\b",
            text.lower(),
        )

        return {
            token
            for token in tokens
            if token not in cls.STOP_WORDS
            and len(token) > 2
        }

    def check(
        self,
        context: str,
        claim: str,
        threshold: float = 0.50,
    ) -> EntailmentResult:

        context_words = self.words(
            context
        )

        claim_words = self.words(
            claim
        )

        if not claim_words:

            return EntailmentResult(
                supported=False,
                score=0.0,
            )

        overlap = (
            claim_words
            & context_words
        )

        score = (
            len(overlap)
            / len(claim_words)
        )

        return EntailmentResult(
            supported=(
                score >= threshold
            ),
            score=score,
        )