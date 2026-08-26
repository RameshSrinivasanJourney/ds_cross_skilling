from dataclasses import dataclass


@dataclass
class RouteDecision:
    model: str
    reason: str


class ModelRouter:
    """Simple rule-based model router."""

    SIMPLE_MODEL = (
        "ollama/llama3.2:3b"
    )

    POWERFUL_MODEL = (
        "ollama/llama3.2:3b"
    )

    def classify(
        self,
        prompt: str,
    ) -> RouteDecision:

        words = prompt.split()

        complex_indicators = [
            "compare",
            "design",
            "architecture",
            "analyze",
            "debug",
            "derive",
            "evaluate",
        ]

        is_complex = (
            len(words) > 25
            or any(
                word.lower()
                in complex_indicators
                for word in words
            )
        )

        if is_complex:

            return RouteDecision(
                model=self.POWERFUL_MODEL,
                reason="complex-task",
            )

        return RouteDecision(
            model=self.SIMPLE_MODEL,
            reason="simple-task",
        )