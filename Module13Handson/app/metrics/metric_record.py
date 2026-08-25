from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class MetricRecord:
    """One observable GenAI request."""

    timestamp: str
    correlation_id: str
    user_id: str
    feature: str
    model: str

    ttft_ms: float | None = None
    total_latency_ms: float | None = None

    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0

    cost: float = 0.0

    success: bool = True
    error_type: str | None = None

    cache_hit: bool = False
    cache_checked: bool = False

    retrieval_relevance: float | None = None
    user_satisfaction: int | None = None

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    @classmethod
    def create(
        cls,
        *,
        correlation_id: str,
        user_id: str,
        feature: str,
        model: str,
    ) -> "MetricRecord":

        return cls(
            timestamp=datetime.now().isoformat(),
            correlation_id=correlation_id,
            user_id=user_id,
            feature=feature,
            model=model,
        )