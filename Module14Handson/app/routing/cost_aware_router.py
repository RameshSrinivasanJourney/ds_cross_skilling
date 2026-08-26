from dataclasses import dataclass

from app.routing.complexity_classifier import (
    ComplexityClassifier,
)


@dataclass(frozen=True)
class RoutingDecision:
    model: str
    complexity: str
    score: int
    reason: str


class CostAwareRouter:
    """
    Select a model based on estimated task complexity.
    """

    def __init__(
        self,
        cheap_model: str = "ollama/llama3.2:3b",
        powerful_model: str = "ollama/llama3.2:3b",
    ) -> None:

        self.cheap_model = cheap_model
        self.powerful_model = (
            powerful_model
        )

        self.classifier = (
            ComplexityClassifier()
        )

    def route(
        self,
        prompt: str,
    ) -> RoutingDecision:

        classification = (
            self.classifier.classify(
                prompt
            )
        )

        if classification.level == "complex":

            return RoutingDecision(
                model=self.powerful_model,
                complexity=(
                    classification.level
                ),
                score=classification.score,
                reason=(
                    "complex-task"
                ),
            )

        return RoutingDecision(
            model=self.cheap_model,
            complexity=(
                classification.level
            ),
            score=classification.score,
            reason=(
                "cost-efficient-route"
            ),
        )