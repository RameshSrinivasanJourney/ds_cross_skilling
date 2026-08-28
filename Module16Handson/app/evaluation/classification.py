from collections import defaultdict


class ClassificationEvaluator:

    def evaluate(
        self,
        actual: list[str],
        predicted: list[str],
    ) -> dict:

        if len(actual) != len(
            predicted
        ):

            raise ValueError(
                "Actual and predicted "
                "lengths must match."
            )

        labels = sorted(
            set(actual)
            | set(predicted)
        )

        per_class = {}

        for label in labels:

            tp = sum(
                a == label
                and p == label
                for a, p in zip(
                    actual,
                    predicted,
                )
            )

            fp = sum(
                a != label
                and p == label
                for a, p in zip(
                    actual,
                    predicted,
                )
            )

            fn = sum(
                a == label
                and p != label
                for a, p in zip(
                    actual,
                    predicted,
                )
            )

            precision = (
                tp / (tp + fp)
                if tp + fp
                else 0.0
            )

            recall = (
                tp / (tp + fn)
                if tp + fn
                else 0.0
            )

            f1 = (
                2
                * precision
                * recall
                / (precision + recall)
                if precision + recall
                else 0.0
            )

            per_class[label] = {
                "precision": precision,
                "recall": recall,
                "f1": f1,
                "support": (
                    tp + fn
                ),
            }

        accuracy = sum(
            a == p
            for a, p in zip(
                actual,
                predicted,
            )
        ) / len(actual)

        macro_f1 = (
            sum(
                item["f1"]
                for item in per_class.values()
            )
            / len(per_class)
        )

        return {
            "accuracy": accuracy,
            "macro_f1": macro_f1,
            "per_class": per_class,
        }