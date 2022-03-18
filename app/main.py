from os import environ
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import fastapi_mail

from .fastapi_socketio import SocketManager,createSocket
from . import isv,fastapi_email
from .database import engine
from .fastapi_email import *

from .isv import models, main

isv.models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(isv.main.router)
app.include_router(fastapi_email.email.router)

# socket io
sio = SocketManager(app=app)
createSocket(sio=sio)