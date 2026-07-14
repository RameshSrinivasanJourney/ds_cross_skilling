from openai import OpenAI
from openai import BadRequestError

from app.config import settings

from app.services.prompt_service import PromptService
from app.services.security_service import SecurityService


class GitHubAIService:

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.GITHUB_TOKEN,
            base_url="https://models.github.ai/inference"
        )

        self.security_service = SecurityService()
        self.prompt_service = PromptService()

    def _build_response(
        self,
        success: bool,
        temperature: float,
        response: str
    ):

        return {
            "success": success,
            "model": settings.MODEL,
            "temperature": temperature,
            "response": response,
            "timestamp": ""
        }

    def generate_response(
        self,
        prompt: str,
        temperature: float = 0.7
    ):

        # -----------------------------------------
        # Validate User Request
        # -----------------------------------------

        is_safe, message = self.security_service.validate_request(prompt)

        if not is_safe:

            return self._build_response(
                False,
                temperature,
                message
            )

        # -----------------------------------------
        # Build Prompt Messages
        # -----------------------------------------

        messages = self.prompt_service.build_messages(
            prompt=prompt,
            max_words=150
        )

        try:

            # -----------------------------------------
            # Call GitHub Models API
            # -----------------------------------------

            response = self.client.chat.completions.create(
                model=settings.MODEL,
                messages=messages,
                temperature=temperature
            )

            answer = response.choices[0].message.content

            # -----------------------------------------
            # Validate AI Response
            # -----------------------------------------

            is_safe, answer = self.security_service.validate_response(
                answer
            )

            if not is_safe:

                return self._build_response(
                    False,
                    temperature,
                    answer
                )

            return self._build_response(
                True,
                temperature,
                answer
            )

        except BadRequestError as ex:

            print(ex)

            return self._build_response(
                False,
                temperature,
                "Your request could not be processed because it violated "
                "the AI provider's safety policy."
            )

        except Exception as ex:

            print(ex)

            return self._build_response(
                False,
                temperature,
                "An unexpected error occurred while contacting the AI service."
            )