from ollama import chat


MODEL_NAME = "llama3.2:3b"


def ask_llm(
    system_prompt: str,
    user_prompt: str,
) -> str:
    """Send a request to the local Ollama model."""

    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
    )

    return response.message.content