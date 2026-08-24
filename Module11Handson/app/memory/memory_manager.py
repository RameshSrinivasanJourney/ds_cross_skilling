from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class EpisodicMemory:
    """Represent an event or experience."""

    event: str
    timestamp: str
    details: dict[str, Any] = field(
        default_factory=dict
    )


@dataclass
class SemanticMemory:
    """Represent a fact or piece of knowledge."""

    key: str
    value: str


@dataclass
class ProceduralMemory:
    """Represent knowledge about how to perform a task."""

    task: str
    steps: list[str]


class MemoryManager:
    """
    Demonstrate five memory types:

    1. In-context / short-term
    2. External / long-term
    3. Episodic
    4. Semantic
    5. Procedural
    """

    def __init__(self):

        # ----------------------------------------
        # 1. Short-term / in-context memory
        # ----------------------------------------

        self.conversation: list[
            dict[str, str]
        ] = []

        # ----------------------------------------
        # 2. External / long-term memory
        # ----------------------------------------

        self.long_term: dict[
            str,
            Any,
        ] = {}

        # ----------------------------------------
        # 3. Episodic memory
        # ----------------------------------------

        self.episodic: list[
            EpisodicMemory
        ] = []

        # ----------------------------------------
        # 4. Semantic memory
        # ----------------------------------------

        self.semantic: dict[
            str,
            SemanticMemory,
        ] = {}

        # ----------------------------------------
        # 5. Procedural memory
        # ----------------------------------------

        self.procedural: dict[
            str,
            ProceduralMemory,
        ] = {}

    # ========================================
    # Short-term memory
    # ========================================

    def add_message(
        self,
        role: str,
        content: str,
    ) -> None:

        self.conversation.append(
            {
                "role": role,
                "content": content,
            }
        )

    def get_context(self) -> list[
        dict[str, str]
    ]:

        return list(
            self.conversation
        )

    # ========================================
    # Long-term memory
    # ========================================

    def save_long_term(
        self,
        key: str,
        value: Any,
    ) -> None:

        self.long_term[key] = value

    def get_long_term(
        self,
        key: str,
    ) -> Any:

        return self.long_term.get(key)

    # ========================================
    # Episodic memory
    # ========================================

    def remember_event(
        self,
        event: str,
        details: dict[str, Any] | None = None,
    ) -> None:

        self.episodic.append(
            EpisodicMemory(
                event=event,
                timestamp=datetime.now().isoformat(),
                details=details or {},
            )
        )

    # ========================================
    # Semantic memory
    # ========================================

    def remember_fact(
        self,
        key: str,
        value: str,
    ) -> None:

        self.semantic[key] = (
            SemanticMemory(
                key=key,
                value=value,
            )
        )

    def get_fact(
        self,
        key: str,
    ) -> str | None:

        memory = self.semantic.get(
            key
        )

        if memory is None:
            return None

        return memory.value

    # ========================================
    # Procedural memory
    # ========================================

    def remember_procedure(
        self,
        task: str,
        steps: list[str],
    ) -> None:

        self.procedural[task] = (
            ProceduralMemory(
                task=task,
                steps=steps,
            )
        )

    def get_procedure(
        self,
        task: str,
    ) -> list[str] | None:

        memory = self.procedural.get(
            task
        )

        if memory is None:
            return None

        return memory.steps