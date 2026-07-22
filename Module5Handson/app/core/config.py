from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # ==========================
    # GitHub Models
    # ==========================

    GITHUB_TOKEN: str

    GITHUB_ENDPOINT: str

    EMBEDDING_MODEL: str


    # ==========================
    # ChromaDB
    # ==========================

    CHROMA_DB_PATH: str = "./chroma_db"

    CHROMA_COLLECTION_NAME: str = "employee_documents"


    class Config:

        env_file = ".env"


settings = Settings()