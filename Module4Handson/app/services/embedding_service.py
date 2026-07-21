from openai import OpenAI

from app.core.config import settings
from app.core.ai_settings import AISettings


client = OpenAI(
    api_key=settings.GITHUB_TOKEN,
    base_url=settings.GITHUB_ENDPOINT
)


class EmbeddingService:

    @staticmethod
    def generate_embedding(text: str):

        response = client.embeddings.create(

            model=AISettings.EMBEDDING_MODEL,

            input=text

        )

        return response.data[0].embedding