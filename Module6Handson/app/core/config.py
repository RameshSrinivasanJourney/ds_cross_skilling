from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # ==========================================================
    # Sentence Transformer
    # ==========================================================

    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    # all-MiniLM-L6-v2 produces 384-dimensional embeddings
    EMBEDDING_DIMENSION: int = 384

    # ==========================================================
    # Ollama
    # ==========================================================

    OLLAMA_MODEL: str = "llama3.2:3b"

    OLLAMA_HOST: str = "http://localhost:11434"

    class Config:
        env_file = ".env"


settings = Settings()