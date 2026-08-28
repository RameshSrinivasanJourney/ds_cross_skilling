import re


class FaithfulnessChecker:
    """
    Lightweight educational faithfulness checker.

    Compares important words in the generated text
    against the supplied source/context.

    This is a baseline metric for learning and is
    not a production-grade factuality evaluator.
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
        "and",
        "or",
        "for",
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
    def _words(
        cls,
        text: str,
    ) -> set[str]:

        words = re.findall(
            r"\b[a-zA-Z0-9]+\b",
            text.lower(),
        )

        return {
            word
            for word in words
            if word not in cls.STOP_WORDS
            and len(word) > 2
        }

    def score(
        self,
        context: str,
        answer: str,
    ) -> float:

        context_words = self._words(
            context
        )

        answer_words = self._words(
            answer
        )

        if not answer_words:
            return 0.0

        supported_words = (
            answer_words
            & context_words
        )

        return (
            len(supported_words)
            / len(answer_words)
        )

    def validate(
        self,
        context: str,
        answer: str,
        threshold: float = 0.35,
    ) -> tuple[bool, float]:

        score = self.score(
            context,
            answer,
        )

        return (
            score >= threshold,
            score,
        )