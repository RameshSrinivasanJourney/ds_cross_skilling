from ollama import Client
from langfuse import observe, propagate_attributes

from app.tracing.langfuse_client import (
    langfuse,
)


MODEL_NAME = "llama3.2:3b"


@observe(
    name="ollama_generation",
    as_type="generation",
)
def generate_with_ollama(
    question: str,
) -> str:

    client = Client(
        host="http://localhost:11434"
    )

    response = client.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
    )

    output = response.message.content

    # Record output on the current generation.
    langfuse.update_current_generation(
        output=output
    )

    return output