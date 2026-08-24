from sentence_transformers import SentenceTransformer


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


class EmbeddingService:
    """Generate embeddings for memory storage and retrieval."""

    def __init__(self):

        self.model = SentenceTransformer(
            MODEL_NAME
        )

    def embed_documents(
        self,
        texts: list[str],
    ):
        """Create embeddings for stored memories."""

        return self.model.encode(
            texts,
            normalize_embeddings=True,
            convert_to_numpy=True,
        )

    def embed_query(
        self,
        query: str,
    ):
        """Create an embedding for a query."""

        return self.model.encode(
            query,
            normalize_embeddings=True,
            convert_to_numpy=True,
        )