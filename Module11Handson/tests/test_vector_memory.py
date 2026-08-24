from app.consolidation.memory_consolidator import (
    consolidate_memories,
)
from app.memory.faiss_memory_store import (
    FAISSMemoryStore,
)


USER_ID = "employee-001"


def test_vector_memory():

    store = FAISSMemoryStore()

    print(
        "\n=== 3.1 STORE USER FACTS ==="
    )

    store.add_memory(
        text=(
            "The user prefers Chennai "
            "as their city."
        ),
        user_id=USER_ID,
        memory_type="semantic",
        importance=1.0,
    )

    store.add_memory(
        text=(
            "The user is a software architect "
            "working on Generative AI."
        ),
        user_id=USER_ID,
        memory_type="semantic",
        importance=1.0,
    )

    print(
        "User facts stored as embeddings."
    )

    print(
        "\n=== 3.2 STORE CONVERSATION SUMMARY ==="
    )

    store.add_memory(
        text=(
            "The user completed Module 10 "
            "Multi-Agent Systems and started "
            "Module 11 Memory Systems."
        ),
        user_id=USER_ID,
        memory_type="episodic",
        importance=0.8,
    )

    print(
        "Conversation summary stored."
    )

    print(
        "\n=== 3.3 RETRIEVE RELEVANT MEMORIES ==="
    )

    query = (
        "Which city does the user prefer?"
    )

    results = store.search(
        query=query,
        user_id=USER_ID,
        top_k=3,
    )

    print(
        f"\nQuery: {query}"
    )

    for result in results:

        print(
            f"\nMemory: "
            f"{result['text']}"
        )

        print(
            f"Type: "
            f"{result['memory_type']}"
        )

        print(
            f"Similarity: "
            f"{result['similarity']:.4f}"
        )

        print(
            f"Freshness: "
            f"{result['freshness']:.4f}"
        )

    print(
        "\n=== 3.4 MEMORY CONSOLIDATION ==="
    )

    active_memories = (
        store.consolidate(
            USER_ID
        )
    )

    consolidated = (
        consolidate_memories(
            active_memories
        )
    )

    for item in consolidated:
        print(item)

    print(
        "\n=== 3.5 MEMORY EXPIRY ==="
    )

    temporary_id = store.add_memory(
        text=(
            "User is currently attending "
            "a temporary training session."
        ),
        user_id=USER_ID,
        memory_type="episodic",
        importance=0.5,
        ttl_days=0,
    )

    print(
        f"Temporary memory ID: "
        f"{temporary_id}"
    )

    removed = store.remove_expired(
        USER_ID
    )

    print(
        f"Expired memories removed: "
        f"{removed}"
    )


if __name__ == "__main__":
    test_vector_memory()