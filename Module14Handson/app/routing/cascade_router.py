from typing import Callable

from app.routing.response_quality import (
    ResponseQualityEvaluator,
)


class CascadeRouter:
    """
    Try a cheaper model first and escalate
    when the response quality is insufficient.
    """

    def __init__(
        self,
        generate: Callable,
        cheap_model: str,
        powerful_model: str,
        quality_threshold: float = 0.6,
    ) -> None:

        self.generate = generate

        self.cheap_model = (
            cheap_model
        )

        self.powerful_model = (
            powerful_model
        )

        self.quality_threshold = (
            quality_threshold
        )

        self.evaluator = (
            ResponseQualityEvaluator()
        )

    def run(
        self,
        prompt: str,
    ) -> dict:

        # -------------------------------------
        # First attempt: cheap model
        # -------------------------------------

        first_result = self.generate(
            prompt,
            model=self.cheap_model,
        )

        first_answer = (
            first_result["answer"]
        )

        first_quality = (
            self.evaluator.evaluate(
                prompt,
                first_answer,
            )
        )

        if (
            first_quality.accepted
            and first_quality.score
            >= self.quality_threshold
        ):

            return {
                "answer": first_answer,
                "selected_model": (
                    self.cheap_model
                ),
                "escalated": False,
                "attempts": 1,
                "quality": (
                    first_quality
                ),
            }

        # -------------------------------------
        # Escalation
        # -------------------------------------

        second_result = self.generate(
            prompt,
            model=self.powerful_model,
        )

        second_answer = (
            second_result["answer"]
        )

        second_quality = (
            self.evaluator.evaluate(
                prompt,
                second_answer,
            )
        )

        return {
            "answer": second_answer,
            "selected_model": (
                self.powerful_model
            ),
            "escalated": True,
            "attempts": 2,
            "first_quality": (
                first_quality
            ),
            "quality": second_quality,
        }