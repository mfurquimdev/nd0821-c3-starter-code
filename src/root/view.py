"""Module describe root's view"""
from typing import Dict

from fastapi import APIRouter
from fastapi import HTTPException
from starlette.responses import JSONResponse

router = APIRouter()


@router.get(
    "/",
    summary="Return basic greeting",
    response_description="Greeting in form of a dictionary",
    response_model=Dict,
)
async def root(fail: bool = False):
    """Root route which returns just a message"""
    if fail:
        raise HTTPException(status_code=404, detail="Fail flag is True")

    return JSONResponse({"greeting": "Hello World!"})
