from app.prompts.system_prompt import SYSTEM_PROMPT
from app.prompts.prompt_builder import build_prompt


class PromptService:

    def build_messages(
        self,
        prompt: str,
        max_words: int = 150
    ):

        return [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": build_prompt(
                    prompt,
                    max_words=max_words
                )
            }
        ]