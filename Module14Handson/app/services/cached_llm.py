import time

from ollama import Client

from app.cache.cache_factory import (
    create_exact_cache,
)


MODEL_NAME = "llama3.2:3b"


class CachedLLM:
    """Ollama service with exact-match caching."""

    def __init__(self):

        self.client = Client(
            host="http://localhost:11434"
        )

        self.cache = (
            create_exact_cache()
        )

    def generate(
        self,
        prompt: str,
    ) -> dict:

        start = time.perf_counter()

        cached = self.cache.get(
            prompt,
            MODEL_NAME,
        )

        if cached is not None:

            latency_ms = (
                time.perf_counter()
                - start
            ) * 1000

            return {
                "answer": cached.response,
                "model": cached.model,
                "cache_hit": True,
                "latency_ms": latency_ms,
                "input_tokens": 0,
                "output_tokens": 0,
                "source": "cache",
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

        answer = (
            response.message.content
        )

        input_tokens = int(
            getattr(
                response,
                "prompt_eval_count",
                0,
            )
            or 0
        )

        output_tokens = int(
            getattr(
                response,
                "eval_count",
                0,
            )
            or 0
        )

        self.cache.set(
            prompt=prompt,
            model=MODEL_NAME,
            response=answer,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
        )

        latency_ms = (
            time.perf_counter()
            - start
        ) * 1000

        return {
            "answer": answer,
            "model": MODEL_NAME,
            "cache_hit": False,
            "latency_ms": latency_ms,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "source": "ollama",
        }