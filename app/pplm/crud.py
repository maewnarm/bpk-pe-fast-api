from sqlalchemy.orm import Session

from . import models, schemas

def get_product(db: Session):
    # return db.query(models.Product).all()
    rs = db.execute("SELECT * FROM strapi.section_strapis")
    rsArray = []
    for row in rs:
        rsArray.append(row)
    return rsArray