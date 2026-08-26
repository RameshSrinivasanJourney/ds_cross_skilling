from typing import Callable


class FallbackRouter:
    """Try models in sequence until one succeeds."""

    def __init__(
        self,
        generate: Callable,
    ):

        self.generate = generate

    def run(
        self,
        prompt: str,
        models: list[str],
    ) -> dict:

        errors = []

        for model in models:

            try:

                result = self.generate(
                    prompt,
                    model=model,
                )

                return {
                    "success": True,
                    "model": model,
                    "result": result,
                    "errors": errors,
                }

            except Exception as exc:

                errors.append(
                    {
                        "model": model,
                        "error": str(exc),
                    }
                )

        return {
            "success": False,
            "model": None,
            "result": None,
            "errors": errors,
        }