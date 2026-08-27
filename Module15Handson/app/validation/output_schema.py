from pydantic import BaseModel, Field


class AnswerResponse(BaseModel):
    answer: str = Field(
        min_length=1,
        max_length=5000,
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
    )

    sources: list[str] = Field(
        default_factory=list,
    )