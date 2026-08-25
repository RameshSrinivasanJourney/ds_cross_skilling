import uuid

from app.metrics.metric_record import (
    MetricRecord,
)
from app.metrics.metrics_collector import (
    MetricsCollector,
)


def build_record(
    *,
    user_id: str,
    feature: str,
    success: bool = True,
    error_type: str | None = None,
    cache_hit: bool = False,
    retrieval_relevance: float | None = None,
    satisfaction: int | None = None,
) -> MetricRecord:

    record = MetricRecord.create(
        correlation_id=str(
            uuid.uuid4()
        ),
        user_id=user_id,
        feature=feature,
        model="llama3.2:3b",
    )

    record.ttft_ms = 200.0
    record.total_latency_ms = 2500.0

    record.input_tokens = 100
    record.output_tokens = 250

    record.success = success
    record.error_type = error_type

    record.cache_checked = True
    record.cache_hit = cache_hit

    record.retrieval_relevance = (
        retrieval_relevance
    )

    record.user_satisfaction = (
        satisfaction
    )

    return record


def test_metrics():

    collector = MetricsCollector()

    print(
        "\n=== RECORD REQUESTS ==="
    )

    records = [
        build_record(
            user_id="user-001",
            feature="rag",
            cache_hit=True,
            retrieval_relevance=0.92,
            satisfaction=5,
        ),
        build_record(
            user_id="user-001",
            feature="chat",
            cache_hit=False,
            retrieval_relevance=0.81,
            satisfaction=4,
        ),
        build_record(
            user_id="user-002",
            feature="rag",
            cache_hit=True,
            retrieval_relevance=0.88,
            satisfaction=4,
        ),
        build_record(
            user_id="user-002",
            feature="chat",
            success=False,
            error_type="timeout",
            cache_hit=False,
            satisfaction=2,
        ),
        build_record(
            user_id="user-003",
            feature="rag",
            cache_hit=True,
            retrieval_relevance=0.95,
            satisfaction=5,
        ),
    ]

    for record in records:

        collector.record(
            record
        )

    print(
        "\n=== SUMMARY ==="
    )

    summary = collector.summary()

    for key, value in summary.items():

        print(
            f"{key}: {value}"
        )

    print(
        "\n=== COST BY USER ==="
    )

    print(
        collector.cost_by_user()
    )

    print(
        "\n=== COST BY FEATURE ==="
    )

    print(
        collector.cost_by_feature()
    )

    # -----------------------------------------
    # Assertions
    # -----------------------------------------

    assert (
        summary["total_requests"] == 5
    )

    assert (
        summary["failed_requests"] == 1
    )

    assert (
        summary["error_rate"] == 0.2
    )

    assert (
        summary["cache_hit_rate"] == 0.6
    )

    assert (
        round(
            summary[
                "average_retrieval_relevance"
            ],
            2,
        )
        == 0.89
    )

    assert (
        round(
            summary[
                "average_user_satisfaction"
            ],
            2,
        )
        == 4.0
    )


if __name__ == "__main__":
    test_metrics()