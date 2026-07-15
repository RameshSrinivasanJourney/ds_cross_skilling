from fastapi import APIRouter

from app.models.chat_models import(ChatRequest, ChatResponse)

from app.prompts.prompt_builder import PromptBuilder

from app.services.ai_service import AIService

from app.services.prompt_engineering_service import PromptEngineeringService

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

    messages = PromptBuilder.build(
        user_prompt
    )

    answer = AIService.ask(
        messages
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

    messages = PromptBuilder.build(
        user_prompt
    )

    answer = AIService.ask(
        messages
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

    messages = PromptBuilder.build(
        user_prompt
    )

    answer = AIService.ask(messages)

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

    messages = PromptBuilder.build(
        user_prompt
    )

    answer = AIService.ask(messages)

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

    messages = PromptBuilder.build(
        user_prompt
    )

    answer = AIService.ask(
        messages
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

    messages = PromptBuilder.build(
        user_prompt
    )

    answer = AIService.ask(
        messages
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

    messages = PromptBuilder.build(
        user_prompt
    )

    answer = AIService.ask(
        messages
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

    messages = PromptBuilder.build(
        user_prompt
    )

    answer = AIService.ask(
        messages
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

    messages = PromptBuilder.build(
        user_prompt
    )

    answer = AIService.ask(
        messages
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

    messages = PromptBuilder.build(
        user_prompt
    )

    answer = AIService.ask(
        messages
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

    messages = PromptBuilder.build(
        user_prompt
    )

    answer = AIService.ask(
        messages
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

    messages = PromptBuilder.build(
        user_prompt
    )

    answer = AIService.ask(
        messages
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

    messages = PromptBuilder.build(
        user_prompt
    )

    answer = AIService.ask(
        messages
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

    messages = PromptBuilder.build(
        user_prompt
    )

    answer = AIService.ask(
        messages
    )

    return ChatResponse(
        response=answer
    )