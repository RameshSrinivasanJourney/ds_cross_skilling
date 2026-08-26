from llmlingua import PromptCompressor


class LLMLinguaCompressor:
    """Wrapper around Microsoft's LLMLingua."""

    def __init__(
        self,
        model_name: str = "microsoft/phi-2",
    ) -> None:

        self.compressor = (
            PromptCompressor(
                model_name
            )
        )

    def compress(
        self,
        prompt: str,
        rate: float = 0.5,
    ) -> str:

        result = (
            self.compressor.compress_prompt(
                prompt,
                rate=rate,
            )
        )

        if isinstance(
            result,
            dict,
        ):

            return result[
                "compressed_prompt"
            ]

        return str(result)