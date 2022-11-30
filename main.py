"""FastAPI app definition"""
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Root route which returns just a message"""
    return {"greeting": "Bye World!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
