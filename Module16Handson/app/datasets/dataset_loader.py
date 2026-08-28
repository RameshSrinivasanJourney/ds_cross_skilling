import json
from pathlib import Path
from typing import Any


def load_json_dataset(
    path: str | Path,
) -> list[dict[str, Any]]:

    dataset_path = Path(path)

    with dataset_path.open(
        "r",
        encoding="utf-8",
    ) as file:

        data = json.load(file)

    if not isinstance(data, list):

        raise ValueError(
            "Dataset must contain a JSON array."
        )

    return data