import json
from datetime import datetime, timedelta
from pathlib import Path

import faiss
import numpy as np

from app.memory.vector_memory import (
    MemoryRecord,
)
from app.retrieval.embedding_service import (
    EmbeddingService,
)


MEMORY_DIR = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "memory_store"
)

INDEX_PATH = MEMORY_DIR / "memories.index"

METADATA_PATH = (
    MEMORY_DIR / "memories.json"
)


class FAISSMemoryStore:
    """FAISS-backed long-term memory store."""

    def __init__(self):

        self.embedding_service = (
            EmbeddingService()
        )

        self.dimension = (
            self.embedding_service
            .embed_query("test")
            .shape[0]
        )

        self.records: list[
            MemoryRecord
        ] = []

        self.index = faiss.IndexFlatIP(
            self.dimension
        )

        self._load()

    # ==========================================
    # Persistence
    # ==========================================

    def _load(self) -> None:

        MEMORY_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        if (
            INDEX_PATH.exists()
            and METADATA_PATH.exists()
        ):

            self.index = faiss.read_index(
                str(INDEX_PATH)
            )

            with METADATA_PATH.open(
                "r",
                encoding="utf-8",
            ) as file:

                data = json.load(file)

            self.records = [
                MemoryRecord(**item)
                for item in data
            ]

    def _save(self) -> None:

        MEMORY_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        faiss.write_index(
            self.index,
            str(INDEX_PATH),
        )

        with METADATA_PATH.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                [
                    record.to_dict()
                    for record in self.records
                ],
                file,
                indent=2,
            )

    # ==========================================
    # 3.1 Store memory
    # ==========================================

    def add_memory(
        self,
        text: str,
        user_id: str,
        memory_type: str,
        importance: float = 1.0,
        ttl_days: int | None = None,
    ) -> int:
        """Embed and store one memory."""

        memory_id = len(
            self.records
        )

        created_at = datetime.now()

        expires_at = None

        if ttl_days is not None:

            expires_at = (
                created_at
                + timedelta(
                    days=ttl_days
                )
            ).isoformat()

        record = MemoryRecord(
            memory_id=memory_id,
            memory_type=memory_type,
            text=text,
            user_id=user_id,
            created_at=created_at.isoformat(),
            expires_at=expires_at,
            importance=importance,
        )

        embedding = (
            self.embedding_service
            .embed_documents([text])
            .astype("float32")
        )

        self.index.add(
            embedding
        )

        self.records.append(
            record
        )

        self._save()

        return memory_id

    # ==========================================
    # 3.3 Retrieve
    # ==========================================

    def search(
        self,
        query: str,
        user_id: str,
        top_k: int = 3,
    ) -> list[dict]:

        if self.index.ntotal == 0:
            return []

        query_embedding = (
            self.embedding_service
            .embed_query(query)
            .astype("float32")
        )

        search_k = min(
            max(top_k * 3, top_k),
            self.index.ntotal,
        )

        scores, indices = (
            self.index.search(
                np.asarray(
                    [query_embedding]
                ),
                search_k,
            )
        )

        results = []

        for score, index in zip(
            scores[0],
            indices[0],
        ):

            if index < 0:
                continue

            record = self.records[
                int(index)
            ]

            if record.user_id != user_id:
                continue

            if record.is_expired():
                continue

            freshness = (
                record.freshness()
            )

            final_score = (
                float(score)
                * 0.8
                + freshness * 0.2
                + record.importance * 0.0
            )

            results.append(
                {
                    "memory_id": (
                        record.memory_id
                    ),
                    "memory_type": (
                        record.memory_type
                    ),
                    "text": record.text,
                    "similarity": float(score),
                    "freshness": freshness,
                    "score": final_score,
                }
            )

        results.sort(
            key=lambda item: item["score"],
            reverse=True,
        )

        return results[:top_k]

    # ==========================================
    # 3.4 Consolidation
    # ==========================================

    def consolidate(
        self,
        user_id: str,
    ) -> list[dict]:
        """Return active memories grouped by type.

        Consolidation here is intentionally simple:
        identify active memories so a higher-level
        process can merge duplicates or related facts.
        """

        active = []

        for record in self.records:

            if record.user_id != user_id:
                continue

            if record.is_expired():
                continue

            active.append(
                record.to_dict()
            )

        return active

    # ==========================================
    # 3.5 Expiry cleanup
    # ==========================================

    def remove_expired(
        self,
        user_id: str,
    ) -> int:
        """
        Remove expired memories by rebuilding the
        FAISS index from active records.
        """

        active_records = [
            record
            for record in self.records
            if not (
                record.user_id == user_id
                and record.is_expired()
            )
        ]

        removed = (
            len(self.records)
            - len(active_records)
        )

        if removed == 0:
            return 0

        self.records = active_records

        texts = [
            record.text
            for record in self.records
        ]

        self.index = faiss.IndexFlatIP(
            self.dimension
        )

        if texts:

            embeddings = (
                self.embedding_service
                .embed_documents(texts)
                .astype("float32")
            )

            self.index.add(
                embeddings
            )

        self._save()

        return removed