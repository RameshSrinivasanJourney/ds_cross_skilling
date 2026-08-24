from app.memory.faiss_memory_store import (
    FAISSMemoryStore,
)


def build_memory_context(
    store: FAISSMemoryStore,
    query: str,
    user_id: str,
    top_k: int = 5,
) -> str:
    """Retrieve relevant memories and format them."""

    memories = store.search(
        query=query,
        user_id=user_id,
        top_k=top_k,
    )

    if not memories:
        return (
            "No relevant long-term memory "
            "was found."
        )

    lines = [
        "Relevant long-term memory:"
    ]

    for memory in memories:

        lines.append(
            f"- [{memory['memory_type']}] "
            f"{memory['text']}"
        )

    return "\n".join(lines)