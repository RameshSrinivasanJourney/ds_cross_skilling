from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class LLMObservation:
    """Metrics and metadata captured for one LLM request."""

    correlation_id: str
    user_id: str
    feature: str
    model: str
    prompt_version: str

    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0

    ttft_ms: float | None = None
    total_latency_ms: float = 0.0

    estimated_cost: float = 0.0

    quality_score: float | None = None
    quality_status: str = "not_evaluated"

    success: bool = True
    error_type: str | None = None
    error_message: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)