from fastapi import APIRouter

from app.models.chat_models import(ChatRequest, ChatResponse)

from app.prompts.prompt_builder import PromptBuilder

from app.services.ai_service import AIService

from app.services.prompt_engineering_service import PromptEngineeringService
from app.services.prompt_execution_service import PromptExecutionService

from app.services.prompt_version_service import PromptVersionService

prompt_router = APIRouter(
    prefix="/prompt",
    tags=["Prompt Engineering"]
)

@prompt_router.post(
    "/implicit",
    response_model=ChatResponse
)
def implicit_prompt(request: ChatRequest):

    user_prompt = PromptEngineeringService.build_implicit_prompt(
        request.message
    )

    answer = (
        PromptExecutionService.execute(
            user_prompt
        )
    )

    return ChatResponse(
        response=answer
    )

@prompt_router.post(
    "/explicit",
    response_model=ChatResponse
)
def explicit_prompt(request: ChatRequest):

    user_prompt = PromptEngineeringService.build_explicit_prompt(
        request.message
    )

    answer = (
        PromptExecutionService.execute(
            user_prompt
        )
    )

    return ChatResponse(
        response=answer
    )

@prompt_router.post(
    "/positive",
    response_model=ChatResponse
)
def positive_prompt(request: ChatRequest):

    user_prompt = PromptEngineeringService.build_positive_prompt(
        request.message
    )

    answer = (
        PromptExecutionService.execute(
            user_prompt
        )
    )

    return ChatResponse(
        response=answer
    )

@prompt_router.post(
    "/negative",
    response_model=ChatResponse
)
def negative_prompt(request: ChatRequest):

    user_prompt = PromptEngineeringService.build_negative_prompt(
        request.message
    )

    answer = (
        PromptExecutionService.execute(
            user_prompt
        )
    )

    return ChatResponse(
        response=answer
    )

@prompt_router.post(
    "/zeroshot",
    response_model=ChatResponse
)
def zero_shot_prompt(request: ChatRequest):

    user_prompt = PromptEngineeringService.build_zero_shot_prompt(
        request.message
    )

    answer = (
        PromptExecutionService.execute(
            user_prompt
        )
    )

    return ChatResponse(
        response=answer
    )

@prompt_router.post(
    "/oneshot",
    response_model=ChatResponse
)
def one_shot_prompt(request: ChatRequest):

    user_prompt = PromptEngineeringService.build_one_shot_prompt(
        request.message
    )

    answer = (
        PromptExecutionService.execute(
            user_prompt
        )
    )

    return ChatResponse(
        response=answer
    )

@prompt_router.post(
    "/fewshot",
    response_model=ChatResponse
)
def few_shot_prompt(request: ChatRequest):

    user_prompt = PromptEngineeringService.build_few_shot_prompt(
        request.message
    )

    answer = (
        PromptExecutionService.execute(
            user_prompt
        )
    )

    return ChatResponse(
        response=answer
    )

@prompt_router.post(
    "/instruction-hierarchy",
    response_model=ChatResponse
)
def instruction_hierarchy(request: ChatRequest):

    user_prompt = (
        PromptEngineeringService
        .build_instruction_hierarchy_prompt(
            request.message
        )
    )

    answer = (
        PromptExecutionService.execute(
            user_prompt
        )
    )

    return ChatResponse(
        response=answer
    )

@prompt_router.post(
    "/chainofthought",
    response_model=ChatResponse
)
def chain_of_thought_prompt(request: ChatRequest):

    user_prompt = (
        PromptEngineeringService
        .build_chain_of_thought_prompt(
            request.message
        )
    )

    answer = (
        PromptExecutionService.execute(
            user_prompt
        )
    )

    return ChatResponse(
        response=answer
    )

@prompt_router.post(
    "/zeroshot-cot",
    response_model=ChatResponse
)
def zero_shot_cot_prompt(request: ChatRequest):

    user_prompt = (
        PromptEngineeringService
        .build_zero_shot_cot_prompt(
            request.message
        )
    )

    answer = (
        PromptExecutionService.execute(
            user_prompt
        )
    )

    return ChatResponse(
        response=answer
    )

@prompt_router.post(
    "/fewshot-cot",
    response_model=ChatResponse
)
def few_shot_cot_prompt(request: ChatRequest):

    user_prompt = (
        PromptEngineeringService
        .build_few_shot_cot_prompt(
            request.message
        )
    )

    answer = (
        PromptExecutionService.execute(
            user_prompt
        )
    )

    return ChatResponse(
        response=answer
    )

@prompt_router.post(
    "/treeofthought",
    response_model=ChatResponse
)
def tree_of_thought_prompt(request: ChatRequest):

    user_prompt = (
        PromptEngineeringService
        .build_tree_of_thought_prompt(
            request.message
        )
    )

    answer = (
        PromptExecutionService.execute(
            user_prompt
        )
    )

    return ChatResponse(
        response=answer
    )

@prompt_router.post(
    "/react",
    response_model=ChatResponse
)
def react_prompt(request: ChatRequest):

    user_prompt = (
        PromptEngineeringService
        .build_react_prompt(
            request.message
        )
    )

    answer = (
        PromptExecutionService.execute(
            user_prompt
        )
    )

    return ChatResponse(
        response=answer
    )

@prompt_router.post(
    "/meta",
    response_model=ChatResponse
)
def meta_prompt(request: ChatRequest):

    user_prompt = (
        PromptEngineeringService
        .build_meta_prompt(
            request.message
        )
    )

    answer = (
        PromptExecutionService.execute(
            user_prompt
        )
    )

    return ChatResponse(
        response=answer
    )

# ==========================================
# Structured Output Prompting
# ==========================================

@prompt_router.post(
    "/json",
    response_model=ChatResponse
)
def json_prompt(request: ChatRequest):

    user_prompt = (
        PromptEngineeringService
        .build_json_prompt(
            request.message
        )
    )

    answer = (
        PromptExecutionService.execute(
            user_prompt
        )
    )

    return ChatResponse(
        response=answer
    )

@prompt_router.post(
    "/xml",
    response_model=ChatResponse
)
def xml_prompt(request: ChatRequest):

    user_prompt = (
        PromptEngineeringService
        .build_xml_prompt(
            request.message
        )
    )

    answer = (
        PromptExecutionService.execute(
            user_prompt
        )
    )

    return ChatResponse(
        response=answer
    )

@prompt_router.post(
    "/markdown",
    response_model=ChatResponse
)
def markdown_prompt(request: ChatRequest):

    user_prompt = (
        PromptEngineeringService
        .build_markdown_prompt(
            request.message
        )
    )

    answer = (
        PromptExecutionService.execute(
            user_prompt
        )
    )

    return ChatResponse(
        response=answer
    )

@prompt_router.post(
    "/fewshot-json",
    response_model=ChatResponse
)
def fewshot_json_prompt(request: ChatRequest):

    user_prompt = (
        PromptEngineeringService
        .build_fewshot_json_prompt(
            request.message
        )
    )

    answer = (
        PromptExecutionService.execute(
            user_prompt
        )
    )

    return ChatResponse(
        response=answer
    )

@prompt_router.post(
    "/json-mode",
    response_model=ChatResponse
)
def json_mode_prompt(request: ChatRequest):

    user_prompt = (
        PromptEngineeringService
        .build_json_mode_prompt(
            request.message
        )
    )

    answer = (
        PromptExecutionService.execute(
            user_prompt
        )
    )

    return ChatResponse(
        response=answer
    )

@prompt_router.post(
    "/schema",
    response_model=ChatResponse
)
def schema_prompt(request: ChatRequest):

    user_prompt = (
        PromptEngineeringService
        .build_schema_prompt(
            request.message
        )
    )

    answer = (
        PromptExecutionService.execute(
            user_prompt
        )
    )

    return ChatResponse(
        response=answer
    )

@prompt_router.post(
    "/tool-extraction",
    response_model=ChatResponse
)
def tool_extraction_prompt(request: ChatRequest):

    user_prompt = (
        PromptEngineeringService
        .build_tool_extraction_prompt(
            request.message
        )
    )

    answer = (
        PromptExecutionService.execute(
            user_prompt
        )
    )

    return ChatResponse(
        response=answer
    )

@prompt_router.post(
    "/ab-test",
    response_model=ChatResponse
)
def ab_test_prompt(request: ChatRequest):

    system_prompt = PromptVersionService.get_prompt_version("v1")
    user_prompt = request.message
    
    answer = (
        PromptEngineeringService.execute_with_system_prompt(
            user_prompt,
            system_prompt
        )
    )

    return ChatResponse(
        response=answer
    )
