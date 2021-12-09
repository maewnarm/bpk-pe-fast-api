from fastapi import Depends, FastAPI, HTTPException

from . import isv, pplm, user
from .database import engine

from .isv import models, main
from .pplm import models, main
from .user import models, main

isv.models.Base.metadata.create_all(bind=engine)
pplm.models.Base.metadata.create_all(bind=engine)
user.models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(isv.main.router)
app.include_router(pplm.main.router)
app.include_router(user.main.router)
