from ollama import Client

from app.safety.safety_classifier import (
    SafetyClassifier,
)

from app.safety.risk_categories import (
    RiskLevel,
)


MODEL_NAME = "llama3.2:3b"


class SafeLLM:

    def __init__(self):

        self.client = Client(
            host="http://localhost:11434"
        )

        self.safety = (
            SafetyClassifier()
        )

    def generate(
        self,
        prompt: str,
    ) -> dict:

        safety_result = (
            self.safety.classify(
                prompt
            )
        )

        if (
            safety_result.level
            == RiskLevel.BLOCK
        ):

            return {
                "status": "blocked",
                "reason": (
                    "Request blocked by "
                    "safety guardrail."
                ),
                "categories": [
                    category.value
                    for category
                    in safety_result.categories
                ],
            }

        if (
            safety_result.level
            == RiskLevel.REVIEW
        ):

            return {
                "status": "review",
                "reason": (
                    "Request requires "
                    "additional safety review."
                ),
                "categories": [
                    category.value
                    for category
                    in safety_result.categories
                ],
            }

        response = self.client.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return {
            "status": "allowed",
            "answer": (
                response.message.content
            ),
        }