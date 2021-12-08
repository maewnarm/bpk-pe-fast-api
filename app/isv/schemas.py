from typing import List, Optional
from datetime import date,time

from pydantic import BaseModel

# isv
class IsvBase(BaseModel): # read and create
    machine_id: int
    date: date
    time: time
    singal: int

class IsvCreate(IsvBase): # create only
    pass


class Isv(IsvBase): # read only
    id: int
    detail: str

    class Config:
        orm_mode = True