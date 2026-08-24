from app.memory.short_term_memory import (
    ShortTermMemory,
)


def print_messages(
    title: str,
    messages,
) -> None:

    print(f"\n=== {title} ===")

    for message in messages:

        print(
            f"{message.role}: "
            f"{message.content}"
        )


def test_short_term_memory():

    memory = ShortTermMemory(
        max_turns=2,
        max_tokens=30,
    )

    # ------------------------------------------
    # Add conversation history
    # ------------------------------------------

    memory.add_message(
        "user",
        "My preferred city is Chennai.",
    )

    memory.add_message(
        "assistant",
        "I will remember your preferred city.",
    )

    memory.add_message(
        "user",
        "I am working on a GenAI project.",
    )

    memory.add_message(
        "assistant",
        "That sounds interesting.",
    )

    memory.add_message(
        "user",
        "I am currently learning multi-agent systems.",
    )

    memory.add_message(
        "assistant",
        "Multi-agent systems use specialized agents.",
    )

    # ------------------------------------------
    # 2.1 Full history
    # ------------------------------------------

    print_messages(
        "2.1 FULL CONVERSATION",
        memory.get_all_messages(),
    )

    # ------------------------------------------
    # 2.2 Last N turns
    # ------------------------------------------

    print_messages(
        "2.2 LAST-N-TURN WINDOW",
        memory.get_last_n_turns(),
    )

    # ------------------------------------------
    # 2.3 Summary
    # ------------------------------------------

    summary = memory.create_summary()

    print("\n=== 2.3 SUMMARY ===")
    print(summary)

    # ------------------------------------------
    # 2.4 Token-aware truncation
    # ------------------------------------------

    token_messages = (
        memory.get_token_limited_messages()
    )

    print_messages(
        "2.4 TOKEN-LIMITED MESSAGES",
        token_messages,
    )

    print(
        "\nEstimated token count:"
    )

    total_tokens = sum(
        memory.estimate_tokens(
            message.content
        )
        for message in token_messages
    )

    print(total_tokens)

    # ------------------------------------------
    # 2.5 Summary buffer
    # ------------------------------------------

    hybrid = (
        memory.get_summary_buffer()
    )

    print(
        "\n=== 2.5 SUMMARY BUFFER ==="
    )

    print(
        "\nOlder Conversation Summary:"
    )

    print(
        hybrid["summary"]
    )

    print(
        "\nRecent Messages:"
    )

    for message in (
        hybrid["recent_messages"]
    ):

        print(
            f"{message.role}: "
            f"{message.content}"
        )


if __name__ == "__main__":
    test_short_term_memory()