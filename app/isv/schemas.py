from typing import List, Optional
from datetime import date, time

from pydantic import BaseModel

# isv
class IsvBase(BaseModel):  # read and create
    pass


class IsvCreate(IsvBase):  # create only
    machine_id: int
    date_: date
    time_: time
    signal: int
    detail: Optional[str]


class Isv(IsvBase):  # read only
    # id: int
    machine_id: str
    date_start: date
    date_end: date
    time_start: time
    time_end: time

    class Config:
        orm_mode = True
