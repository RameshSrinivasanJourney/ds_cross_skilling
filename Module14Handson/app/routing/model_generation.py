from litellm import completion


def generate(
    prompt: str,
    *,
    model: str,
) -> dict:

    response = completion(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    message = (
        response.choices[0].message
    )

    usage = getattr(
        response,
        "usage",
        None,
    )

    return {
        "answer": (
            message.content
            or ""
        ),
        "input_tokens": (
            getattr(
                usage,
                "prompt_tokens",
                0,
            )
            or 0
        ),
        "output_tokens": (
            getattr(
                usage,
                "completion_tokens",
                0,
            )
            or 0
        ),
    }