import json


def parse_json(response: str):
    try:
        return json.loads(response)

    except json.JSONDecodeError:
        return None