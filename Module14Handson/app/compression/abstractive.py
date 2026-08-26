from ollama import Client


MODEL_NAME = "llama3.2:3b"


class AbstractiveCompressor:
    """Compress text by asking Ollama to rewrite it."""

    def __init__(
        self,
        model: str = MODEL_NAME,
    ) -> None:

        self.client = Client(
            host="http://localhost:11434"
        )

        self.model = model

    def compress(
        self,
        text: str,
        question: str,
    ) -> str:

        prompt = f"""
Compress the following context for an AI assistant.

Preserve all facts necessary to answer the question.
Remove repetition and unnecessary wording.
Do not invent facts.
Keep the compressed version substantially shorter.

Question:
{question}

Context:
{text}

Compressed context:
""".strip()

        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return (
            response.message.content
            .strip()
        )