from dataclasses import dataclass


@dataclass
class CompressionMetrics:
    original_chars: int
    compressed_chars: int

    original_words: int
    compressed_words: int

    compression_ratio: float
    reduction_percent: float


def calculate_metrics(
    original: str,
    compressed: str,
) -> CompressionMetrics:

    original_words = len(
        original.split()
    )

    compressed_words = len(
        compressed.split()
    )

    if compressed_words == 0:

        ratio = 0.0

    else:

        ratio = (
            original_words
            / compressed_words
        )

    if original_words == 0:

        reduction = 0.0

    else:

        reduction = (
            1
            - (
                compressed_words
                / original_words
            )
        ) * 100

    return CompressionMetrics(
        original_chars=len(
            original
        ),
        compressed_chars=len(
            compressed
        ),
        original_words=original_words,
        compressed_words=compressed_words,
        compression_ratio=ratio,
        reduction_percent=reduction,
    )