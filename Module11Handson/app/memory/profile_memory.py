from app.memory.faiss_memory_store import (
    FAISSMemoryStore,
)


def seed_user_profile(
    store: FAISSMemoryStore,
    user_id: str,
) -> None:
    """Store durable user profile memories."""

    store.add_memory(
        text="The user prefers Chennai as their city.",
        user_id=user_id,
        memory_type="user_profile",
        importance=1.0,
    )

    store.add_memory(
        text=(
            "The user is a software architect "
            "working with .NET and cloud technologies."
        ),
        user_id=user_id,
        memory_type="user_profile",
        importance=1.0,
    )