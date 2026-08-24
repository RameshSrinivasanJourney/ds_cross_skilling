from collections import defaultdict


def consolidate_memories(
    memories: list[dict],
) -> list[str]:
    """
    Create a simple consolidated view.

    In a production system, an LLM could perform
    semantic merging of related memories.
    """

    grouped: dict[
        str,
        list[str],
    ] = defaultdict(list)

    for memory in memories:

        grouped[
            memory["memory_type"]
        ].append(
            memory["text"]
        )

    consolidated = []

    for memory_type, texts in (
        grouped.items()
    ):

        consolidated.append(
            f"{memory_type}: "
            + " | ".join(texts)
        )

    return consolidated