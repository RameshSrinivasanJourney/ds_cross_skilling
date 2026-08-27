import json
from typing import Any

from pydantic import ValidationError

from app.validation.faithfulness import (
    FaithfulnessChecker,
)

from app.validation.output_policy import (
    OutputPolicyValidator,
)

from app.validation.output_rules import (
    OutputRuleValidator,
)

from app.validation.output_schema import (
    AnswerResponse,
)

from app.validation.post_processor import (
    OutputPostProcessor,
)


class OutputValidationResult:

    def __init__(
        self,
        valid: bool,
        output: str,
        errors: list[str],
        faithfulness_score: float | None = None,
    ) -> None:

        self.valid = valid
        self.output = output
        self.errors = errors
        self.faithfulness_score = (
            faithfulness_score
        )


class OutputValidator:
    """Run output validation pipeline."""

    def __init__(self):

        self.rules = (
            OutputRuleValidator()
        )

        self.policy = (
            OutputPolicyValidator()
        )

        self.faithfulness = (
            FaithfulnessChecker()
        )

        self.post_processor = (
            OutputPostProcessor()
        )

    def validate_text(
        self,
        output: str,
        *,
        context: str | None = None,
    ) -> OutputValidationResult:

        cleaned = (
            self.post_processor.process(
                output
            )
        )

        errors = []

        # Rule checks
        errors.extend(
            self.rules.validate(
                cleaned
            )
        )

        # Content policy
        errors.extend(
            self.policy.validate(
                cleaned
            )
        )

        # Faithfulness
        faithfulness_score = None

        if context:

            faithful, score = (
                self.faithfulness.validate(
                    context,
                    cleaned,
                )
            )

            faithfulness_score = score

            if not faithful:

                errors.append(
                    "Output failed the "
                    "faithfulness threshold."
                )

        errors = list(
            dict.fromkeys(
                errors
            )
        )

        return OutputValidationResult(
            valid=not errors,
            output=cleaned,
            errors=errors,
            faithfulness_score=(
                faithfulness_score
            ),
        )

    def validate_json(
        self,
        output: str,
    ) -> AnswerResponse:

        parsed: Any = json.loads(
            output
        )

        return AnswerResponse.model_validate(
            parsed
        )