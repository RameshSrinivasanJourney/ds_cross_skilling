from openai import OpenAI

from app.core.config import settings


class StreamingService:

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.GITHUB_TOKEN,
            base_url=settings.GITHUB_ENDPOINT
        )

    def stream_chat(self, messages):
        """
        Stream response from GitHub Models.
        """

        pass