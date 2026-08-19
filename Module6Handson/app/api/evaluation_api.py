from fastapi import APIRouter

from app.services.evaluation_service import (
    EvaluationService
)


router = APIRouter(
    prefix="/rag",
    tags=["RAG Evaluation"]
)


# ==========================================================
# RAG Evaluation
# ==========================================================

@router.post(
    "/evaluate"
)
def evaluate():

    response = EvaluationService.evaluate(
        top_k=5
    )

    return response