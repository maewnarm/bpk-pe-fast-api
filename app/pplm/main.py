from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from . import crud
from ..dependencies import get_db

router = APIRouter(prefix="/pplm")


@router.get("/product")
async def get_machines(db:Session = Depends(get_db)):
    return crud.get_product(db)
