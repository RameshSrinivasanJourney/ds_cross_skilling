from sentence_transformers import (
    SentenceTransformer
)

from app.core.config import settings


class EmbeddingService:

    model = SentenceTransformer(
        settings.EMBEDDING_MODEL
    )

    # ==========================================================
    # Single Embedding
    # ==========================================================

    @classmethod
    def generate_embedding(
        cls,
        text: str
    ):

        embedding = cls.model.encode(
            text
        )

        return embedding.tolist()

    # ==========================================================
    # Batch Embeddings
    # ==========================================================

    @classmethod
    def generate_embeddings(
        cls,
        texts: list[str]
    ):

        embeddings = cls.model.encode(
            texts,

            batch_size=32,

            show_progress_bar=False
        )

        return embeddings.tolist()