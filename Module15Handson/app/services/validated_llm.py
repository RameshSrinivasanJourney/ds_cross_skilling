from ollama import Client

from app.validation.input_validator import (
    InputValidator,
)


MODEL_NAME = "llama3.2:3b"


class ValidatedLLM:

    def __init__(self):

        self.client = Client(
            host="http://localhost:11434"
        )

        self.validator = (
            InputValidator()
        )

    def generate(
        self,
        prompt: str,
    ) -> dict:

        validation = (
            self.validator.validate(
                prompt
            )
        )

        if not validation.valid:

            return {
                "status": "rejected",
                "categories": (
                    validation.categories
                ),
                "reasons": (
                    validation.reasons
                ),
            }

        response = self.client.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": (
                        validation.normalized_text
                    ),
                }
            ],
        )

        return {
            "status": "allowed",
            "answer": (
                response.message.content
            ),
            "normalized_input": (
                validation.normalized_text
            ),
        }