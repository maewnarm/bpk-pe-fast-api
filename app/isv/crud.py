from fastapi.param_functions import Depends
from sqlalchemy.orm import Session

from . import models, schemas


def get_all_record(db: Session):
    return db.query(models.Operation_record).all()


def get_records(db: Session, param: schemas.Isv):
    machinesid = param.machine_id.split(",")
    machinesid = [int(i) for i in machinesid]
    return (
        db.query(models.Operation_record)
        .filter(
            models.Operation_record.machine_id.in_(machinesid),
            models.Operation_record.date_.between(param.date_start, param.date_end),
            models.Operation_record.time_.between(param.time_start, param.time_end),
        )
        .order_by(
            models.Operation_record.machine_id,
            models.Operation_record.date_,
            models.Operation_record.time_,
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
