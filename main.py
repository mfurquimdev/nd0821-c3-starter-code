"""FastAPI app definition"""
import uvicorn
from fastapi import FastAPI

from src.root.view import router as root_router

app = FastAPI()

app.include_router(root_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
