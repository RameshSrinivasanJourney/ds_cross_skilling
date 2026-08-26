import time
import uuid
from dataclasses import dataclass

from ollama import Client


MODEL_NAME = "llama3.2:3b"


@dataclass
class RequestMetric:
    request_id: str
    question: str
    latency_ms: float
    input_tokens: int
    output_tokens: int
    total_tokens: int
    llm_called: bool


class LLMBenchmark:
    """Measure LLM calls with and without caching."""

    def __init__(
        self,
        model: str = MODEL_NAME,
    ) -> None:

        self.client = Client(
            host="http://localhost:11434"
        )

        self.model = model

    def generate(
        self,
        question: str,
    ) -> tuple[str, RequestMetric]:

        request_id = str(
            uuid.uuid4()
        )

        start = time.perf_counter()

        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
        )

        elapsed = (
            time.perf_counter()
            - start
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

        metric = RequestMetric(
            request_id=request_id,
            question=question,
            latency_ms=(
                elapsed * 1000
            ),
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=(
                input_tokens
                + output_tokens
            ),
            llm_called=True,
        )

        return (
            response.message.content,
            metric,
        )