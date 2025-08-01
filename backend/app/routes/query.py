from fastapi import APIRouter, Body
from openai import OpenAI  # ✅ New import
import os

router = APIRouter()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # ✅ Updated initialization

@router.post("/query")
async def query_llm(data: dict = Body(...)):
    question = data.get("question", "")
    if not question:
        return {"response": "No question provided."}

    try:
        response = client.chat.completions.create(  # ✅ Updated method call
            model="gpt-4",  # or use "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            max_tokens=200,
            temperature=0.7
        )

        answer = response.choices[0].message.content.strip()  # ✅ Access the new-style object
        return {"response": answer}

    except Exception as e:
        return {"response": f"Error: {str(e)}"}
