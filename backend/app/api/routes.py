from fastapi import APIRouter
from ..models.schemas import QueryRequest, QueryResponse
from ..services.llm import get_llm_response

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
async def handle_query(payload: QueryRequest):
    result = await get_llm_response(payload.question)
    return {"response": result}

@router.get("/chat")
async def health_check():
    return {"message": "LLMPawa Backend is live"}
