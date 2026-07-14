import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

    MODEL = os.getenv(
        "GITHUB_MODEL",
        "openai/gpt-4.1"
    )


settings = Settings()