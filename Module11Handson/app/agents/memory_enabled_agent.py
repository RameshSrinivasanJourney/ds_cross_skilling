from ollama import chat

from app.memory.faiss_memory_store import (
    FAISSMemoryStore,
)
from app.retrieval.memory_context_builder import (
    build_memory_context,
)


MODEL_NAME = "llama3.2:3b"


class MemoryEnabledAgent:
    """Ollama agent with retrieved long-term memory."""

    def __init__(
        self,
        user_id: str,
        store: FAISSMemoryStore,
    ):
        self.user_id = user_id
        self.store = store

    def ask(
        self,
        question: str,
    ) -> str:
        """Retrieve memory and ask the local LLM."""

        memory_context = (
            build_memory_context(
                store=self.store,
                query=question,
                user_id=self.user_id,
            )
        )

        system_prompt = (
            "You are a helpful personalized assistant.\n\n"
            "Use the relevant long-term memory below "
            "when it helps answer the user.\n"
            "Treat memories as contextual information, "
            "not unquestionable truth.\n"
            "Do not invent personal facts.\n\n"
            f"{memory_context}"
        )

        response = chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": question,
                },
            ],
        )

        return response.message.content