from openai import OpenAI

from app.core.config import settings
from app.core.ai_settings import AISettings

from app.services.conversation_service import ConversationService
from app.services.exception_service import ExceptionService
from app.utils.logger import logger
from app.utils.token_counter import TokenCounter
from app.security.output_filter import OutputFilter

client = OpenAI(
    api_key=settings.GITHUB_TOKEN,
    base_url=settings.GITHUB_ENDPOINT
)

class AIService:
    
    @staticmethod
    def ask(messages=None, json_mode=False):

        if messages is None:
            messages = ConversationService.get_messages()

            token_count = TokenCounter.count_tokens(messages)

            logger.info(f"Prompt Tokens : {token_count}")

        try:

            logger.info("Sending request to GitHub AI")

            kwargs = {}

            if json_mode:
                kwargs["response_format"] = {
                    "type": "json_object"
                }

            response = client.chat.completions.create(

                model=AISettings.MODEL_NAME,

                messages=messages,

                **kwargs

            )

            logger.info("Received response from GitHub AI")

            answer = response.choices[0].message.content

            return OutputFilter.filter(
                answer
            )
    
        except Exception as ex:
            logger.error(f"AI Service Error: {ex}")
            return ExceptionService.handle(ex)
