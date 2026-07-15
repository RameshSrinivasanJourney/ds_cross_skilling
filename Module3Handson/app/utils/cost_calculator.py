class Costcalculator:
    INPUT_PRICE = 0.15 / 1_000_000

    OUTPUT_PRICE = 0.60 / 1_000_000

    @staticmethod
    def calculate_cost(
        input_tokens: int,
        output_tokens: int
    ):
        input_cost = (
            input_tokens * Costcalculator.INPUT_PRICE
        )

        output_cost = (
            output_tokens * Costcalculator.OUTPUT_PRICE
        )

        return round(
            input_cost + output_cost, 6
        )