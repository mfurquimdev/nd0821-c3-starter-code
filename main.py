#!/bin/env python
"""FastAPI app definition"""
import os
import pickle

import dvc.api
import uvicorn
from dvc.api import DVCFileSystem
from fastapi import FastAPI

from src.infer.view import router as infer_router
from src.root.view import router as root_router

if "DYNO" in os.environ and os.path.isdir(".dvc"):
    os.system("dvc config core.no_scm true")
    if os.system("dvc pull") != 0:
        exit("dvc pull failed")
    os.system("rm -r .dvc .apt/usr/lib/dvc")

app = FastAPI()

app.include_router(root_router)
app.include_router(infer_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
