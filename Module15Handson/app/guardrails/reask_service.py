from ollama import Client

from app.guardrails.custom_validators import (
    NoPIIValidator,
)


MODEL_NAME = "llama3.2:3b"


class ReaskService:

    def __init__(
        self,
        max_reasks: int = 2,
    ) -> None:

        self.client = Client(
            host="http://localhost:11434"
        )

        self.validator = (
            NoPIIValidator()
        )

        self.max_reasks = max_reasks

    def generate(
        self,
        prompt: str,
    ) -> dict:

        current_prompt = prompt

        for attempt in range(
            self.max_reasks + 1
        ):

            response = self.client.chat(
                model=MODEL_NAME,
                messages=[
                    {
                        "role": "user",
                        "content": current_prompt,
                    }
                ],
            )

            answer = (
                response.message.content
            )

            try:

                self.validator.validate(
                    answer
                )

                return {
                    "status": "valid",
                    "answer": answer,
                    "attempts": attempt + 1,
                }

            except ValueError as exc:

                if (
                    attempt
                    >= self.max_reasks
                ):

                    return {
                        "status": "failed",
                        "answer": answer,
                        "attempts": (
                            attempt + 1
                        ),
                        "error": str(exc),
                    }

                current_prompt = f"""
Regenerate your answer.

Your previous answer failed validation:
{exc}

Do not include personally identifiable
information.

Original request:
{prompt}
""".strip()

        return {
            "status": "failed",
            "answer": "",
            "attempts": (
                self.max_reasks + 1
            ),
        }