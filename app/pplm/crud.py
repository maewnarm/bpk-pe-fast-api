from sqlalchemy.orm import Session

from . import models, schemas

def get_product(db: Session):
    return db.query(models.Product).all()