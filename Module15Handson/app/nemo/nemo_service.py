from pathlib import Path

from nemoguardrails import (
    LLMRails,
    RailsConfig,
)


CONFIG_PATH = Path(
    __file__
).parent / "config"


class NemoGuardrailService:
    """NeMo Guardrails wrapper."""

    def __init__(self) -> None:

        config = (
            RailsConfig.from_path(
                str(CONFIG_PATH)
            )
        )

        self.rails = LLMRails(
            config
        )

    async def generate(
        self,
        message: str,
    ) -> str:

        response = await (
            self.rails.generate_async(
                messages=[
                    {
                        "role": "user",
                        "content": message,
                    }
                ]
            )
        )

        if hasattr(
            response,
            "response",
        ):

            return response.response

        return str(response)