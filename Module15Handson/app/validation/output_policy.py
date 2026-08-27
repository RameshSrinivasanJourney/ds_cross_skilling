from app.safety.safety_classifier import (
    SafetyClassifier,
)

from app.safety.risk_categories import (
    RiskLevel,
)


class OutputPolicyValidator:
    """Check LLM output against safety policy."""

    def __init__(self):

        self.classifier = (
            SafetyClassifier()
        )

    def validate(
        self,
        output: str,
    ) -> list[str]:

        result = (
            self.classifier.classify(
                output
            )
        )

        errors = []

        if (
            result.level
            == RiskLevel.BLOCK
        ):

            errors.append(
                "Output violates the "
                "configured safety policy."
            )

        elif (
            result.level
            == RiskLevel.REVIEW
        ):

            errors.append(
                "Output requires "
                "safety review."
            )

        return errors