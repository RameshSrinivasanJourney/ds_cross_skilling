from app.core.ai_settings import AISettings
import tiktoken


class TokenCounter:

    @staticmethod
    def count_tokens(messages):

        encoding = tiktoken.get_encoding(AISettings.TOKEN_ENCODING)

        total_tokens = 0

        for message in messages:

            total_tokens += len(
                encoding.encode(
                    message.get("content", "")
                )
            )

        return total_tokens