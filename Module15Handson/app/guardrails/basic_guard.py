from guardrails import Guard
from pydantic import BaseModel


class Answer(BaseModel):
    answer: str


answer_guard = Guard.for_pydantic(
    output_class=Answer
)