from pydantic import BaseModel


class EmbeddingRequest(BaseModel):

    text: str


class EmbeddingResponse(BaseModel):

    dimensions: int

    embedding: list[float]

    model: str