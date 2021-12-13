from fastapi import Depends, FastAPI, HTTPException

from . import isv
from .database import engine

from .isv import models, main

isv.models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(isv.main.router)
