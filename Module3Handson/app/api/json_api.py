from fastapi import APIRouter

from app.models.chat_models import ChatRequest

from app.prompts.prompt_builder import PromptBuilder

from app.services.ai_service import AIService

from app.services.prompt_engineering_service import (
    PromptEngineeringService
)

from app.utils.json_parser import JsonParser

json_router = APIRouter(
    prefix="/json",
    tags=["JSON Validation"]
)


@json_router.post("/validate")
def validate_json(request: ChatRequest):

    user_prompt = (
        PromptEngineeringService
        .build_json_prompt(
            request.message
        )
    )

    messages = PromptBuilder.build(
        user_prompt
    )

    answer = AIService.ask(
        messages
    )

    parsed = JsonParser.parse(answer)

    return {

        "raw_response": answer,

        "is_valid_json": parsed is not None,

        "parsed_json": parsed

    }