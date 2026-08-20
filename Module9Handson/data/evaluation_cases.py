EVALUATION_CASES = [
    {
        "question": (
            "What is the current weather "
            "in Chennai?"
        ),
        "expected_tools": [
            "get_weather"
        ],
        "expected_steps": 1,
    },
    {
        "question": (
            "What is the current weather "
            "in London?"
        ),
        "expected_tools": [
            "get_weather"
        ],
        "expected_steps": 1,
    },
    {
        "question": (
            "What is the current weather "
            "in Mumbai?"
        ),
        "expected_tools": [
            "get_weather"
        ],
        "expected_steps": 1,
    },
]