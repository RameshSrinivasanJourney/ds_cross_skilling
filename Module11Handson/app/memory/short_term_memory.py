from dataclasses import dataclass
from typing import Any


@dataclass
class Message:
    """Represent one conversation message."""

    role: str
    content: str


class ShortTermMemory:
    """
    Demonstrate short-term memory management:

    1. Full message history
    2. Last-N-turn window
    3. Summarization
    4. Token-aware truncation
    5. Summary buffer
    """

    def __init__(
        self,
        max_turns: int = 3,
        max_tokens: int = 120,
    ):
        self.messages: list[Message] = []

        self.max_turns = max_turns

        self.max_tokens = max_tokens

        self.summary = ""

    # ==========================================
    # 2.1 Full conversation history
    # ==========================================

    def add_message(
        self,
        role: str,
        content: str,
    ) -> None:

        self.messages.append(
            Message(
                role=role,
                content=content,
            )
        )

    def get_all_messages(
        self,
    ) -> list[Message]:

        return list(
            self.messages
        )

    # ==========================================
    # Utility
    # ==========================================

    @staticmethod
    def estimate_tokens(
        text: str,
    ) -> int:
        """
        Lightweight token approximation.

        This is only an educational estimate.
        """

        if not text:
            return 0

        return max(
            1,
            (len(text) + 3) // 4,
        )

    # ==========================================
    # 2.2 Last-N-turn window
    # ==========================================

    def get_last_n_turns(
        self,
    ) -> list[Message]:

        # A turn is considered a user + assistant
        # pair, so keep 2 * N messages.
        message_count = (
            self.max_turns * 2
        )

        return self.messages[
            -message_count:
        ]

    # ==========================================
    # 2.3 Summarization
    # ==========================================

    def create_summary(
        self,
    ) -> str:

        if not self.messages:
            return ""

        lines = []

        for message in self.messages:

            lines.append(
                f"{message.role}: "
                f"{message.content}"
            )

        text = "\n".join(lines)

        # Educational deterministic summary.
        # A real application can call an LLM
        # to summarize this text.
        self.summary = (
            "Conversation summary:\n"
            + text
        )

        return self.summary

    # ==========================================
    # 2.4 Token-aware truncation
    # ==========================================

    def get_token_limited_messages(
        self,
    ) -> list[Message]:

        selected: list[Message] = []

        total_tokens = 0

        # Start with most recent messages.
        for message in reversed(
            self.messages
        ):

            message_tokens = (
                self.estimate_tokens(
                    message.content
                )
            )

            if (
                total_tokens
                + message_tokens
                > self.max_tokens
            ):
                break

            selected.insert(
                0,
                message,
            )

            total_tokens += (
                message_tokens
            )

        return selected

    # ==========================================
    # 2.5 Hybrid summary buffer
    # ==========================================

    def get_summary_buffer(
        self,
    ) -> dict[str, Any]:

        recent_messages = (
            self.get_last_n_turns()
        )

        old_messages = self.messages[
            : -len(recent_messages)
        ] if recent_messages else self.messages

        if old_messages:
            old_text = "\n".join(
                f"{message.role}: "
                f"{message.content}"
                for message in old_messages
            )

            summary = (
                "Summary of older conversation:\n"
                + old_text
            )

        else:
            summary = self.summary

        return {
            "summary": summary,
            "recent_messages": recent_messages,
        }