from litellm import completion


OLLAMA_MODEL = "ollama/llama3.2:3b"


class LiteLLMService:
    """Common LLM interface through LiteLLM."""

    def generate(
        self,
        prompt: str,
        model: str = OLLAMA_MODEL,
    ) -> dict:

        response = completion(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        message = response.choices[0].message

        usage = getattr(
            response,
            "usage",
            None,
        )

        return {
            "model": model,
            "answer": message.content,
            "input_tokens": (
                getattr(
                    usage,
                    "prompt_tokens",
                    0,
                )
                or 0
            ),
            "output_tokens": (
                getattr(
                    usage,
                    "completion_tokens",
                    0,
                )
                or 0
            ),
        }