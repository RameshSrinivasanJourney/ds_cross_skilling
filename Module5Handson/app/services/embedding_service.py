from sentence_transformers import SentenceTransformer

from app.core.config import settings


class EmbeddingService:

    model = SentenceTransformer(

        settings.SENTENCE_TRANSFORMER_MODEL

    )


    @classmethod
    def generate_embedding(

        cls,

        text: str

    ):

        embedding = cls.model.encode(

            text,

            convert_to_numpy=True

        )

        return embedding.tolist()