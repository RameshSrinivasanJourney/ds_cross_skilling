from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # ==========================
    # GitHub Models
    # ==========================

    GITHUB_TOKEN: str

    GITHUB_ENDPOINT: str

    EMBEDDING_MODEL: str

    # ==========================
    # Sentence Transformers
    # ==========================

    SENTENCE_TRANSFORMER_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    # ==========================
    # ChromaDB
    # ==========================

    CHROMA_DB_PATH: str = "./chroma_db"

    CHROMA_COLLECTION_NAME: str = "employee_documents"

    # ==========================
    # Qdrant
    # ==========================

    QDRANT_API_KEY: str
    QDRANT_URL: str
    QDRANT_COLLECTION: str = "employee_documents"
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333

    # ==========================
    # FAISS - Sentence Transformer
    # ==========================

    FAISS_ST_INDEX_PATH: str = "./faiss_st_index"
    FAISS_ST_DIMENSION: int = 384

    class Config:

        env_file = ".env"


settings = Settings()