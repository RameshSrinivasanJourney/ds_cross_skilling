from abc import ABC, abstractmethod
from typing import Any


class StateStore(ABC):
    """Common interface for external state stores."""

    @abstractmethod
    def save(
        self,
        key: str,
        value: dict[str, Any],
    ) -> None:
        """Save state."""
        raise NotImplementedError

    @abstractmethod
    def get(
        self,
        key: str,
    ) -> dict[str, Any] | None:
        """Retrieve state."""
        raise NotImplementedError