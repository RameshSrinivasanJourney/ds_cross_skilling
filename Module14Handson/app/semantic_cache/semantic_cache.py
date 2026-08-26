import math
import time
from dataclasses import dataclass


@dataclass
class SemanticCacheEntry:
    query: str
    embedding: list[float]
    response: str
    model: str
    created_at: float


class SemanticCache:
    """Local semantic cache using embedding similarity."""

    def __init__(
        self,
        embedding_service,
        threshold: float = 0.85,
    ) -> None:

        self.embedding_service = (
            embedding_service
        )

        self.threshold = threshold

        self.entries: list[
            SemanticCacheEntry
        ] = []

    @staticmethod
    def cosine_similarity(
        vector_a: list[float],
        vector_b: list[float],
    ) -> float:

        dot_product = sum(
            a * b
            for a, b in zip(
                vector_a,
                vector_b,
            )
        )

        magnitude_a = math.sqrt(
            sum(
                a * a
                for a in vector_a
            )
        )

        magnitude_b = math.sqrt(
            sum(
                b * b
                for b in vector_b
            )
        )

        if (
            magnitude_a == 0
            or magnitude_b == 0
        ):
            return 0.0

        return (
            dot_product
            / (
                magnitude_a
                * magnitude_b
            )
        )

    def lookup(
        self,
        query: str,
        model: str,
    ) -> tuple[
        SemanticCacheEntry | None,
        float,
    ]:

        if not self.entries:
            return None, 0.0

        query_embedding = (
            self.embedding_service.embed(
                query
            )
        )

        best_entry = None
        best_score = 0.0

        for entry in self.entries:

            if entry.model != model:
                continue

            score = self.cosine_similarity(
                query_embedding,
                entry.embedding,
            )

            if score > best_score:

                best_score = score
                best_entry = entry

        if (
            best_entry is not None
            and best_score
            >= self.threshold
        ):

            return (
                best_entry,
                best_score,
            )

        return None, best_score

    def store(
        self,
        query: str,
        response: str,
        model: str,
    ) -> None:

        embedding = (
            self.embedding_service.embed(
                query
            )
        )

        self.entries.append(
            SemanticCacheEntry(
                query=query,
                embedding=embedding,
                response=response,
                model=model,
                created_at=time.time(),
            )
        )

    def clear(self) -> None:

        self.entries.clear()

    def size(self) -> int:
        return len(
            self.entries
        )