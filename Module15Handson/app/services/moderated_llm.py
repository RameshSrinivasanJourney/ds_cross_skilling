from ollama import Client

from app.moderation.categories import (
    ModerationDecision,
)

from app.moderation.classifier import (
    ModerationClassifier,
)


MODEL_NAME = "llama3.2:3b"


class ModeratedLLM:

    def __init__(self):

        self.client = Client(
            host="http://localhost:11434"
        )

        self.moderator = (
            ModerationClassifier()
        )

    def generate(
        self,
        prompt: str,
    ) -> dict:

        # -----------------------------
        # Input moderation
        # -----------------------------

        input_result = (
            self.moderator.classify(
                prompt
            )
        )

        if (
            input_result.decision
            != ModerationDecision.ALLOW
        ):

            return {
                "status": "blocked",
                "stage": "input",
                "decision": (
                    input_result.decision.value
                ),
                "categories": [
                    category.value
                    for category
                    in input_result.categories
                ],
                "reason": (
                    input_result.reason
                ),
            }

        # -----------------------------
        # LLM
        # -----------------------------

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

        # -----------------------------
        # Output moderation
        # -----------------------------

        output_result = (
            self.moderator.classify(
                answer
            )
        )

        if (
            output_result.decision
            != ModerationDecision.ALLOW
        ):

            return {
                "status": "blocked",
                "stage": "output",
                "decision": (
                    output_result.decision.value
                ),
                "categories": [
                    category.value
                    for category
                    in output_result.categories
                ],
                "reason": (
                    output_result.reason
                ),
            }

        return {
            "status": "allowed",
            "answer": answer,
            "input_moderation": (
                input_result.decision.value
            ),
            "output_moderation": (
                output_result.decision.value
            ),
        }