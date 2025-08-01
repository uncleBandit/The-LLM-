import os
from dotenv import load_dotenv
from openai import AsyncOpenAI  # ✅ Modern OpenAI SDK

load_dotenv()

# ✅ Initialize the async client with OpenRouter base
client = AsyncOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

async def get_llm_response(question: str) -> str:
    try:
        response = await client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",  # ✅ Free OpenRouter model
            messages=[{"role": "user", "content": question}],
            max_tokens=500,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "Error reaching LLM: " + str(e)
