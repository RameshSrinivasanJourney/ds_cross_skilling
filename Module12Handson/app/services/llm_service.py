import asyncio
from collections.abc import Iterator

from ollama import Client

from app.core.config import (
    OLLAMA_HOST,
    OLLAMA_MODEL,
)
from app.core.exceptions import (
    LLMServiceError,
)


class LLMService:
    """Application service for local Ollama."""

    def __init__(self):

        self.client = Client(
            host=OLLAMA_HOST
        )

        self.model = OLLAMA_MODEL

    def generate(
        self,
        question: str,
    ) -> str:

        try:

            response = self.client.chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": question,
                    }
                ],
            )

            return response.message.content

        except Exception as exc:

            raise LLMServiceError(
                "The LLM service could not "
                "generate a response."
            ) from exc

    async def generate_async(
        self,
        question: str,
    ) -> str:

        return await asyncio.to_thread(
            self.generate,
            question,
        )

    def stream(
        self,
        question: str,
    ) -> Iterator[str]:

        try:

            response = self.client.chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": question,
                    }
                ],
                stream=True,
            )

            for chunk in response:

                content = (
                    chunk.message.content
                )

                if content:
                    yield content

        except Exception as exc:

            raise LLMServiceError(
                "The LLM streaming service failed."
            ) from exc