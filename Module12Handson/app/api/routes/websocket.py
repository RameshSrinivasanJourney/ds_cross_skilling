import asyncio

from fastapi import (
    APIRouter,
    WebSocket,
    WebSocketDisconnect,
)

from app.services.llm_service import (
    LLMService,
)


router = APIRouter(
    tags=["websocket"]
)


@router.websocket(
    "/ws/chat"
)
async def websocket_chat(
    websocket: WebSocket,
):

    await websocket.accept()

    llm = LLMService()

    try:

        while True:

            question = (
                await websocket.receive_text()
            )

            await websocket.send_json(
                {
                    "type": "status",
                    "message": (
                        "Generating response..."
                    ),
                }
            )

            answer = await llm.generate_async(
                question
            )

            await websocket.send_json(
                {
                    "type": "answer",
                    "content": answer,
                }
            )

    except WebSocketDisconnect:

        pass