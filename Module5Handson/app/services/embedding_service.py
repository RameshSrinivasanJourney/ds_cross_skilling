from openai import OpenAI

from app.core.config import settings


class EmbeddingService:

    client = OpenAI(

        base_url=settings.GITHUB_ENDPOINT,

        api_key=settings.GITHUB_TOKEN

    )

    @classmethod
    def generate_embedding(

        cls,

        text: str

    ):

        response = cls.client.embeddings.create(

            model=settings.EMBEDDING_MODEL,

            input=text

        )

        return response.data[0].embedding