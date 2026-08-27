import json

from ollama import Client
from pydantic import ValidationError

from app.validation.output_validator import (
    OutputValidator,
)


MODEL_NAME = "llama3.2:3b"


class OutputValidatedLLM:

    def __init__(self):

        self.client = Client(
            host="http://localhost:11434"
        )

        self.validator = (
            OutputValidator()
        )

    def generate_text(
        self,
        prompt: str,
        *,
        context: str | None = None,
    ) -> dict:

        response = self.client.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        answer = (
            response.message.content
        )

        validation = (
            self.validator.validate_text(
                answer,
                context=context,
            )
        )

        if not validation.valid:

            return {
                "status": "rejected",
                "answer": validation.output,
                "errors": validation.errors,
                "faithfulness_score": (
                    validation.faithfulness_score
                ),
            }

        return {
            "status": "valid",
            "answer": validation.output,
            "errors": [],
            "faithfulness_score": (
                validation.faithfulness_score
            ),
        }

    def generate_json(
        self,
        prompt: str,
    ) -> dict:

        response = self.client.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            format="json",
        )

        raw = (
            response.message.content
        )

        try:

            parsed = self.validator.validate_json(
                raw
            )

            return {
                "status": "valid",
                "result": parsed.model_dump(),
            }

        except (
            json.JSONDecodeError,
            ValidationError,
        ) as exc:

            return {
                "status": "invalid",
                "raw": raw,
                "error": str(exc),
            }