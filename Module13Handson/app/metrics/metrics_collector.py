from collections import defaultdict
from statistics import mean
from typing import Any

from app.metrics.metric_record import (
    MetricRecord,
)
from app.metrics.pricing import (
    calculate_cost,
)


class MetricsCollector:
    """Collect and aggregate GenAI metrics."""

    def __init__(self):

        self.records: list[
            MetricRecord
        ] = []

    # ==========================================
    # Record one request
    # ==========================================

    def record(
        self,
        metric: MetricRecord,
    ) -> None:

        metric.total_tokens = (
            metric.input_tokens
            + metric.output_tokens
        )

        metric.cost = calculate_cost(
            model=metric.model,
            input_tokens=metric.input_tokens,
            output_tokens=metric.output_tokens,
        )

        self.records.append(
            metric
        )

    # ==========================================
    # 4.4 Error rate
    # ==========================================

    def error_rate(self) -> float:

        if not self.records:
            return 0.0

        failures = sum(
            1
            for record in self.records
            if not record.success
        )

        return (
            failures
            / len(self.records)
        )

    def error_breakdown(
        self,
    ) -> dict[str, int]:

        breakdown = defaultdict(int)

        for record in self.records:

            if not record.success:

                breakdown[
                    record.error_type
                    or "unknown"
                ] += 1

        return dict(breakdown)

    # ==========================================
    # 4.5 Cache hit rate
    # ==========================================

    def cache_hit_rate(self) -> float:

        checked = [
            record
            for record in self.records
            if record.cache_checked
        ]

        if not checked:
            return 0.0

        hits = sum(
            1
            for record in checked
            if record.cache_hit
        )

        return (
            hits
            / len(checked)
        )

    # ==========================================
    # 4.6 Retrieval relevance
    # ==========================================

    def average_relevance(
        self,
    ) -> float:

        scores = [
            record.retrieval_relevance
            for record in self.records
            if record.retrieval_relevance
            is not None
        ]

        if not scores:
            return 0.0

        return mean(scores)

    # ==========================================
    # 4.7 User satisfaction
    # ==========================================

    def average_satisfaction(
        self,
    ) -> float:

        scores = [
            record.user_satisfaction
            for record in self.records
            if record.user_satisfaction
            is not None
        ]

        if not scores:
            return 0.0

        return mean(scores)

    # ==========================================
    # Latency
    # ==========================================

    def average_ttft_ms(
        self,
    ) -> float:

        values = [
            record.ttft_ms
            for record in self.records
            if record.ttft_ms
            is not None
        ]

        if not values:
            return 0.0

        return mean(values)

    def average_latency_ms(
        self,
    ) -> float:

        values = [
            record.total_latency_ms
            for record in self.records
            if record.total_latency_ms
            is not None
        ]

        if not values:
            return 0.0

        return mean(values)

    # ==========================================
    # Tokens / cost
    # ==========================================

    def total_input_tokens(
        self,
    ) -> int:

        return sum(
            record.input_tokens
            for record in self.records
        )

    def total_output_tokens(
        self,
    ) -> int:

        return sum(
            record.output_tokens
            for record in self.records
        )

    def total_tokens(
        self,
    ) -> int:

        return sum(
            record.total_tokens
            for record in self.records
        )

    def total_cost(
        self,
    ) -> float:

        return sum(
            record.cost
            for record in self.records
        )

    # ==========================================
    # Per-user aggregation
    # ==========================================

    def cost_by_user(
        self,
    ) -> dict[str, float]:

        result = defaultdict(float)

        for record in self.records:

            result[
                record.user_id
            ] += record.cost

        return dict(result)

    # ==========================================
    # Per-feature aggregation
    # ==========================================

    def cost_by_feature(
        self,
    ) -> dict[str, float]:

        result = defaultdict(float)

        for record in self.records:

            result[
                record.feature
            ] += record.cost

        return dict(result)

    # ==========================================
    # Summary
    # ==========================================

    def summary(
        self,
    ) -> dict[str, Any]:

        successful = sum(
            1
            for record in self.records
            if record.success
        )

        failed = (
            len(self.records)
            - successful
        )

        return {
            "total_requests": len(
                self.records
            ),
            "successful_requests": (
                successful
            ),
            "failed_requests": failed,
            "error_rate": (
                self.error_rate()
            ),
            "average_ttft_ms": (
                self.average_ttft_ms()
            ),
            "average_latency_ms": (
                self.average_latency_ms()
            ),
            "input_tokens": (
                self.total_input_tokens()
            ),
            "output_tokens": (
                self.total_output_tokens()
            ),
            "total_tokens": (
                self.total_tokens()
            ),
            "total_cost": (
                self.total_cost()
            ),
            "cache_hit_rate": (
                self.cache_hit_rate()
            ),
            "average_retrieval_relevance": (
                self.average_relevance()
            ),
            "average_user_satisfaction": (
                self.average_satisfaction()
            ),
            "error_breakdown": (
                self.error_breakdown()
            ),
        }