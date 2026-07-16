from app.prompts.prompt_builder import PromptBuilder
from app.services.ai_service import AIService


class PromptExecutionService:

    @staticmethod
    def execute(user_prompt: str):

        messages = PromptBuilder.build(
            user_prompt
        )

        return AIService.ask(
            messages
        )

    @staticmethod
    def execute_with_system_prompt(
        user_prompt: str,
        system_prompt: str
    ):

        messages = PromptBuilder.build(
            user_prompt=user_prompt,
            system_prompt=system_prompt
        )

        return AIService.ask(
            messages
        )