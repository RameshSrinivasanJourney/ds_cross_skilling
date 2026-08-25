from dataclasses import dataclass


@dataclass(frozen=True)
class ModelPricing:
    """Pricing per 1 million tokens."""

    input_per_1m: float
    output_per_1m: float


MODEL_PRICING = {
    "llama3.2:3b": ModelPricing(
        input_per_1m=0.0,
        output_per_1m=0.0,
    ),
}


def calculate_cost(
    model: str,
    input_tokens: int,
    output_tokens: int,
) -> float:
    """Calculate estimated model cost."""

    pricing = MODEL_PRICING.get(
        model
    )

    if pricing is None:
        return 0.0

    input_cost = (
        input_tokens
        / 1_000_000
        * pricing.input_per_1m
    )

    output_cost = (
        output_tokens
        / 1_000_000
        * pricing.output_per_1m
    )

    return input_cost + output_cost