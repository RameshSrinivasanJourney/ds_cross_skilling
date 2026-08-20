from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application configuration settings."""

    ollama_host: str = "http://localhost:11434"
    ollama_model: str = "llama3.2:3b"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()