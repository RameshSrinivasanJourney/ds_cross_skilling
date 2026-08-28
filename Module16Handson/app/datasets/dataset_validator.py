from typing import Any


REQUIRED_GOLDEN_FIELDS = {
    "id",
    "question",
    "expected_answer",
    "required_facts",
}


def validate_golden_dataset(
    dataset: list[dict[str, Any]],
) -> list[str]:

    errors: list[str] = []

    seen_ids: set[str] = set()

    for index, item in enumerate(dataset):

        missing = (
            REQUIRED_GOLDEN_FIELDS
            - set(item.keys())
        )

        if missing:

            errors.append(
                f"Item {index} is missing: "
                f"{sorted(missing)}"
            )

        item_id = item.get("id")

        if not item_id:

            errors.append(
                f"Item {index} has no id."
            )

        elif item_id in seen_ids:

            errors.append(
                f"Duplicate id: {item_id}"
            )

        else:

            seen_ids.add(item_id)

        if not isinstance(
            item.get("required_facts"),
            list,
        ):

            errors.append(
                f"Item {index} required_facts "
                f"must be a list."
            )

    return errors