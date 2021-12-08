from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas, isv, pplm
from .database import SessionLocal, engine

from .isv import models, main
from .pplm import models, main

models.Base.metadata.create_all(bind=engine)
isv.models.Base.metadata.create_all(bind=engine)
pplm.models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(isv.main.router)
app.include_router(pplm.main.router)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/sections/", response_model=List[schemas.Section])
def read_sections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sections = crud.get_sections(db=db, skip=skip, limit=limit)
    return sections


@app.post("/sections/", response_model=schemas.Section)
def create_section(section: schemas.SectionCreate, db: Session = Depends(get_db)):
    db_section = crud.get_section_by_code(db, section.code)
    if db_section:
        raise HTTPException(status_code=400, detail="Code already registered")
    return crud.create_section(db, section)
