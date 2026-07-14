from openai import OpenAI

from app.core.config import settings

from app.services.conversation_service import ConversationService

client = OpenAI(
    api_key=settings.GITHUB_TOKEN,
    base_url=settings.GITHUB_ENDPOINT
)

class AIService:
    
    @staticmethod
    def ask():

        messages = ConversationService.get_messages()

        response = client.chat.completions.create(

            model="openai/gpt-4.1-mini",

            messages=messages

        )

        return response.choices[0].message.content