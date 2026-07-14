from app.services.github_ai_service import GitHubAIService


class AIService:

    def __init__(self):
        self.github_service = GitHubAIService()

    def get_response(
        self,
        prompt: str,
        model: str,
        temperature: float
    ):
        return self.github_service.generate_response(
            prompt,
            temperature
        )