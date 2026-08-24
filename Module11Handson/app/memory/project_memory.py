from app.memory.faiss_memory_store import (
    FAISSMemoryStore,
)


def seed_project_context(
    store: FAISSMemoryStore,
    user_id: str,
) -> None:
    """Store project-specific context."""

    store.add_memory(
        text=(
            "The user is currently studying "
            "Module 11 Memory Systems."
        ),
        user_id=user_id,
        memory_type="project_context",
        importance=1.0,
    )

    store.add_memory(
        text=(
            "The user completed Module 10 "
            "Multi-Agent Systems."
        ),
        user_id=user_id,
        memory_type="project_context",
        importance=0.9,
    )

    store.add_memory(
        text=(
            "The user has already implemented "
            "FAISS memory retrieval and LangGraph "
            "checkpointing."
        ),
        user_id=user_id,
        memory_type="project_context",
        importance=0.9,
    )