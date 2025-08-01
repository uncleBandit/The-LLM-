from fastapi import APIRouter, HTTPException
from app.schemas import QueryRequest, QueryResponse
from app.prompts import generate_response

router = APIRouter()

@router.post("/ask", response_model=QueryResponse)
async def ask_question(payload: QueryRequest):
    try:
        answer = await generate_response(payload.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
