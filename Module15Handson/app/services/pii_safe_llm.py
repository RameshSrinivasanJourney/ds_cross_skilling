from ollama import Client

from app.pii.token_mapper import (
    PIITokenMapper,
)


MODEL_NAME = "llama3.2:3b"


class PIISafeLLM:
    """Hide PII from the model and restore it afterward."""

    def __init__(self) -> None:

        self.client = Client(
            host="http://localhost:11434"
        )

    def generate(
        self,
        user_message: str,
    ) -> dict:

        mapper = PIITokenMapper()

        safe_message = (
            mapper.replace(
                user_message
            )
        )

        prompt = f"""
Answer the user's request.

The input may contain placeholders such as
<EMAIL_1> or <PHONE_1>. Preserve those
placeholders exactly when referring to them.

Do not attempt to reconstruct the original
private information.

User request:
{safe_message}
""".strip()

        response = self.client.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        model_response = (
            response.message.content
        )

        restored_response = (
            mapper.restore(
                model_response
            )
        )

        return {
            "original_input": user_message,
            "safe_input": safe_message,
            "model_response": model_response,
            "final_response": restored_response,
            "pii_tokens": dict(
                mapper.mapping
            ),
        }