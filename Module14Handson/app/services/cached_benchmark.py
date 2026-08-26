import time

from app.cache.exact_cache import (
    ExactCache,
)
from app.services.llm_benchmark import (
    LLMBenchmark,
    RequestMetric,
)


class CachedBenchmark:
    """Benchmark an LLM with an exact-match cache."""

    def __init__(self):

        self.llm = LLMBenchmark()

        self.cache = ExactCache()

    def generate(
        self,
        question: str,
    ) -> tuple[str, RequestMetric, bool]:

        start = time.perf_counter()

        cached = self.cache.get(
            question
        )

        if cached is not None:

            elapsed = (
                time.perf_counter()
                - start
            )

            metric = RequestMetric(
                request_id="cache-hit",
                question=question,
                latency_ms=(
                    elapsed * 1000
                ),
                input_tokens=0,
                output_tokens=0,
                total_tokens=0,
                llm_called=False,
            )

            return (
                cached.response,
                metric,
                True,
            )

        response, metric = (
            self.llm.generate(
                question
            )
        )

        self.cache.set(
            prompt=question,
            response=response,
            input_tokens=(
                metric.input_tokens
            ),
            output_tokens=(
                metric.output_tokens
            ),
        )

        return (
            response,
            metric,
            False,
        )