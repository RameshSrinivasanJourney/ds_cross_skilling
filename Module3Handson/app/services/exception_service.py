from openai import AuthenticationError
from openai import RateLimitError
from openai import NotFoundError
from openai import APIError


class ExceptionService:

    @staticmethod
    def handle(exception: Exception) -> str:

        if isinstance(exception, AuthenticationError):
            return "Invalid GitHub API Token."

        if isinstance(exception, NotFoundError):
            return "Requested AI model was not found."

        if isinstance(exception, RateLimitError):
            return "GitHub API rate limit exceeded."

        if isinstance(exception, APIError):
            return "GitHub AI service is currently unavailable."

        return f"Unexpected Error : {str(exception)}"