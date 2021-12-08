from sqlalchemy.orm import Session
from sqlalchemy.sql.sqltypes import String

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.employee_id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreally"
    db_user = models.User(
        employee_id=user.employee_id,
        section_code=user.section_code,
        email=user.email,
        hashed_password=fake_hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_sections(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Section).offset(skip).limit(limit).all()


def get_section_by_code(db: Session, code: str):
    return db.query(models.Section).filter(models.Section.code == code).first()


def create_section(db: Session, section: schemas.SectionCreate):
    db_section = models.Section(**section.dict())
    db.add(db_section)
    db.commit()
    db.refresh(db_section)
    return db_section
