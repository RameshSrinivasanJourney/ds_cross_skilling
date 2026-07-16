from app.prompts.system_prompt import SYSTEM_PROMPT
from app.services.context_service import ContextService


class PromptBuilder:

    @staticmethod
    def build(
        user_message: str,
        system_prompt: str = None
    ):

        if system_prompt is None:
            system_prompt = SYSTEM_PROMPT

        context = ContextService.get_employee_context()

        messages = [

            {
                "role": "system",
                "content": system_prompt
            },

            {
                "role": "user",
                "content": f"""
                Employee Context:

                {context}

                Question:

                {user_message}
                """
            }
        ]

        return messages