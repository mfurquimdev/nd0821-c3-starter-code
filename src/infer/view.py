"""Module describe infer's view"""
from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from src.infer.model import InferData
from src.infer.model import InferResponse
from starlette.responses import JSONResponse

router = APIRouter(
    prefix="/infer",
    tags=["inference", "prediction"],
)


@router.post(
    "/",
    summary="Make inference/prediction on a given data",
    response_description="Array of predictions whether the salary is greater than 50K",
    response_model=InferResponse,
)
async def root(request: list[InferData]) -> InferResponse:
    """Root route which returns just a message"""

    return JSONResponse({"greeting": "Hello World!"})
