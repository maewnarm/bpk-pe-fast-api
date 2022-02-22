from fastapi.param_functions import Depends
from sqlalchemy.orm import Session

from . import models, schemas


def get_all_record(db: Session):
    return db.query(models.Operation_record).all()


def get_records(db: Session, param: schemas.IsvRead):
    machinesid = param.machine_id.split(",")
    machinesid = [int(i) for i in machinesid]
    print(param)
    return (
        db.query(models.Operation_record)
        .filter(
            models.Operation_record.machine_id.in_(machinesid),
            models.Operation_record.datetime_.between(param.datetime_start, param.datetime_end),
        )
        .order_by(
            models.Operation_record.machine_id,
            models.Operation_record.datetime_,
        )
        .all()
    )


def create_record(db: Session, record: schemas.IsvCreate):
    print(record)
    db_record = models.Operation_record(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
