from sqlalchemy.orm import Session

from . import models, schemas

def get_all_record(db: Session):
    return db.query(models.Operation_record).all()