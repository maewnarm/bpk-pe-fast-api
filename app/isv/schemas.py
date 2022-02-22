from typing import List, Optional
from datetime import datetime,date

from pydantic import BaseModel

# isv
class IsvBase(BaseModel):  # read and create
    pass


class IsvCreate(IsvBase):  # create only
    machine_id: int
    datetime_: datetime
    signal: int
    detail: Optional[str]


class IsvRead(IsvBase):  # read only
    # id: int
    machine_id: str
    datetime_start: datetime
    datetime_end: datetime

    class Config:
        orm_mode = True
