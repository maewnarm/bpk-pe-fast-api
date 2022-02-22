from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional

from . import crud, schemas
from ..dependencies import get_db

router = APIRouter(prefix="/isv")


@router.get("/")
async def get_all_record(db: Session = Depends(get_db), skip: int = 0):
    print(skip)
    return crud.get_all_record(db)


@router.get("/records/")  # response_model=schemas.Isv
async def get_records(param: schemas.IsvRead = Depends(), db: Session = Depends(get_db)):
    print(param)
    return crud.get_records(db, param)


@router.post("/records/")
async def create_record(record: schemas.IsvCreate, db: Session = Depends(get_db)):
    return crud.create_record(db, record)
