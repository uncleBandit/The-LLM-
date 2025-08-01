from fastapi import FastAPI
from app.api import router
import uvicorn

app = FastAPI(title="LLmPawa API", version="1.0")

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

@app.get("/")
def read_root():
    return {"message": "LLmPawa API is running"}