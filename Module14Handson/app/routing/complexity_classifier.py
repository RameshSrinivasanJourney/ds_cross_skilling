from dataclasses import dataclass


@dataclass(frozen=True)
class ComplexityResult:
    score: int
    level: str
    reasons: list[str]


class ComplexityClassifier:
    """Classify a task before selecting a model."""

    COMPLEXITY_KEYWORDS = {
        "architect",
        "architecture",
        "compare",
        "design",
        "evaluate",
        "analyze",
        "debug",
        "derive",
        "optimize",
        "trade-off",
        "tradeoffs",
        "distributed",
        "scalable",
        "multi-tenant",
        "implementation",
        "reason",
    }

    def classify(
        self,
        prompt: str,
    ) -> ComplexityResult:

        text = prompt.lower().strip()

        words = text.split()

        score = 0
        reasons: list[str] = []

        # Length signal
        if len(words) > 40:

            score += 2

            reasons.append(
                "long_prompt"
            )

        elif len(words) > 20:

            score += 1

            reasons.append(
                "moderate_prompt_length"
            )

        # Complexity keywords
        matches = [
            keyword
            for keyword in self.COMPLEXITY_KEYWORDS
            if keyword in text
        ]

        if matches:

            score += min(
                len(matches),
                4,
            )

            reasons.append(
                "complexity_keywords:"
                + ",".join(matches)
            )

        # Multiple-task signal
        task_markers = [
            " and ",
            " then ",
            " step ",
            "steps",
            "first",
            "second",
            "third",
        ]

        task_count = sum(
            1
            for marker in task_markers
            if marker in text
        )

        if task_count >= 2:

            score += 2

            reasons.append(
                "multiple_task_indicators"
            )

        # Question/analysis signal
        analytical_markers = [
            "why",
            "how would you",
            "what are the trade",
            "explain why",
            "pros and cons",
            "advantages and disadvantages",
        ]

        if any(
            marker in text
            for marker in analytical_markers
        ):

            score += 2

            reasons.append(
                "analytical_reasoning"
            )

        if score >= 5:

            level = "complex"

        elif score >= 2:

            level = "medium"

        else:

            level = "simple"

        return ComplexityResult(
            score=score,
            level=level,
            reasons=reasons,
        )