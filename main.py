from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Larissa": "Aceita casar comigo? ❤️"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
