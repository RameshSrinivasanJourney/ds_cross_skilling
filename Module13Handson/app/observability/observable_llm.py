import hashlib
import time
import uuid
from collections.abc import Iterator
from typing import Any

from ollama import Client

from app.observability.metrics import (
    LLMObservation,
)
from app.observability.structured_logger import (
    configure_logging,
)


MODEL_NAME = "llama3.2:3b"

PROMPT_VERSION = "v1"

# Ollama is running locally, so the default
# estimated cost is zero.
INPUT_COST_PER_1M = 0.0
OUTPUT_COST_PER_1M = 0.0


class ObservableLLM:
    """LLM wrapper that captures observability metrics."""

    def __init__(
        self,
        model: str = MODEL_NAME,
    ) -> None:

        self.client = Client(
            host="http://localhost:11434"
        )

        self.model = model
        self.logger = configure_logging()

    @staticmethod
    def _prompt_hash(
        prompt: str,
    ) -> str:

        return hashlib.sha256(
            prompt.encode("utf-8")
        ).hexdigest()[:16]

    @staticmethod
    def _calculate_cost(
        input_tokens: int,
        output_tokens: int,
    ) -> float:

        input_cost = (
            input_tokens
            / 1_000_000
            * INPUT_COST_PER_1M
        )

        output_cost = (
            output_tokens
            / 1_000_000
            * OUTPUT_COST_PER_1M
        )

        return input_cost + output_cost

    @staticmethod
    def _evaluate_quality(
        answer: str,
    ) -> tuple[float, str]:

        if not answer.strip():
            return 0.0, "poor"

        lowered = answer.lower()

        failure_phrases = [
            "i don't know",
            "i cannot answer",
            "error",
            "failed to generate",
        ]

        if any(
            phrase in lowered
            for phrase in failure_phrases
        ):

            return 0.3, "degraded"

        if len(answer.strip()) < 30:

            return 0.6, "acceptable"

        return 1.0, "good"

    def generate(
        self,
        question: str,
        *,
        user_id: str = "anonymous",
        feature: str = "chat",
        prompt_version: str = PROMPT_VERSION,
    ) -> tuple[str, LLMObservation]:

        correlation_id = str(
            uuid.uuid4()
        )

        prompt = (
            "You are a helpful assistant.\n\n"
            f"User question:\n{question}"
        )

        observation = LLMObservation(
            correlation_id=correlation_id,
            user_id=user_id,
            feature=feature,
            model=self.model,
            prompt_version=prompt_version,
        )

        start = time.perf_counter()

        self.logger.info(
            "llm_request_started",
            extra={
                "observation": {
                    "correlation_id": correlation_id,
                    "user_id": user_id,
                    "feature": feature,
                    "model": self.model,
                    "prompt_version": prompt_version,
                    "prompt_hash": (
                        self._prompt_hash(
                            prompt
                        )
                    ),
                }
            },
        )

        try:

            response = self.client.chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )

            elapsed = (
                time.perf_counter()
                - start
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

            observation.input_tokens = (
                input_tokens
            )

            observation.output_tokens = (
                output_tokens
            )

            observation.total_tokens = (
                input_tokens
                + output_tokens
            )

            observation.total_latency_ms = (
                elapsed * 1000
            )

            observation.estimated_cost = (
                self._calculate_cost(
                    input_tokens,
                    output_tokens,
                )
            )

            quality_score, quality_status = (
                self._evaluate_quality(
                    answer
                )
            )

            observation.quality_score = (
                quality_score
            )

            observation.quality_status = (
                quality_status
            )

            self.logger.info(
                "llm_request_completed",
                extra={
                    "observation": (
                        observation.to_dict()
                        | {
                            "prompt_hash": (
                                self._prompt_hash(
                                    prompt
                                )
                            )
                        }
                    )
                },
            )

            return answer, observation

        except Exception as exc:

            observation.success = False

            observation.error_type = (
                type(exc).__name__
            )

            observation.error_message = (
                str(exc)
            )

            observation.total_latency_ms = (
                (
                    time.perf_counter()
                    - start
                )
                * 1000
            )

            self.logger.error(
                "llm_request_failed",
                extra={
                    "observation": (
                        observation.to_dict()
                    )
                },
            )

            raise

    def stream(
        self,
        question: str,
        *,
        user_id: str = "anonymous",
        feature: str = "chat",
        prompt_version: str = PROMPT_VERSION,
    ) -> tuple[
        Iterator[str],
        dict[str, Any],
    ]:

        correlation_id = str(
            uuid.uuid4()
        )

        prompt = (
            "You are a helpful assistant.\n\n"
            f"User question:\n{question}"
        )

        start = time.perf_counter()

        first_chunk_time: float | None = None
        chunk_count = 0

        metadata: dict[str, Any] = {
            "correlation_id": correlation_id,
            "user_id": user_id,
            "feature": feature,
            "model": self.model,
            "prompt_version": prompt_version,
            "prompt_hash": (
                self._prompt_hash(prompt)
            ),
            "ttft_ms": None,
            "total_latency_ms": None,
            "chunk_count": 0,
            "input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": 0,
        }

        self.logger.info(
            "llm_stream_started",
            extra={
                "observation": metadata.copy()
            },
        )

        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            stream=True,
        )

        def generator() -> Iterator[str]:

            nonlocal first_chunk_time
            nonlocal chunk_count

            try:

                for chunk in response:

                    content = (
                        chunk.message.content
                    )

                    if not content:
                        continue

                    chunk_count += 1

                    if first_chunk_time is None:

                        first_chunk_time = (
                            time.perf_counter()
                        )

                        metadata[
                            "ttft_ms"
                        ] = (
                            first_chunk_time
                            - start
                        ) * 1000

                    metadata[
                        "chunk_count"
                    ] = chunk_count

                    # Ollama may provide token
                    # counters on the final chunk.
                    prompt_eval_count = (
                        getattr(
                            chunk,
                            "prompt_eval_count",
                            None,
                        )
                    )

                    eval_count = getattr(
                        chunk,
                        "eval_count",
                        None,
                    )

                    if (
                        prompt_eval_count
                        is not None
                    ):
                        metadata[
                            "input_tokens"
                        ] = int(
                            prompt_eval_count
                        )

                    if eval_count is not None:
                        metadata[
                            "output_tokens"
                        ] = int(
                            eval_count
                        )

                    yield content

                end = time.perf_counter()

                metadata[
                    "total_latency_ms"
                ] = (
                    end - start
                ) * 1000

                metadata[
                    "total_tokens"
                ] = (
                    metadata[
                        "input_tokens"
                    ]
                    + metadata[
                        "output_tokens"
                    ]
                )

                self.logger.info(
                    "llm_stream_completed",
                    extra={
                        "observation": (
                            metadata.copy()
                        )
                    },
                )

            except Exception as exc:

                metadata[
                    "total_latency_ms"
                ] = (
                    time.perf_counter()
                    - start
                ) * 1000

                metadata[
                    "error_type"
                ] = type(exc).__name__

                metadata[
                    "error_message"
                ] = str(exc)

                self.logger.error(
                    "llm_stream_failed",
                    extra={
                        "observation": (
                            metadata.copy()
                        )
                    },
                )

                raise

        return generator(), metadata