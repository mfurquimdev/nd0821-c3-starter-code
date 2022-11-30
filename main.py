from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Larissa": "Aceita casar comigo? ❤️"}
