from typing import List, Optional
from datetime import date, time

from pydantic import BaseModel

# Product
class ProductBase(BaseModel):  # read and create
    name: str


class ProductCreate(ProductBase):  # create only
    pass


class Product(ProductBase):  # read only
    id: int

    class Config:
        orm_mode = True


# Part
class PartBase(BaseModel):  # read and create
    name: str
    product_id: int


class PartCreate(PartBase):  # create only
    pass


class Part(PartBase):  # read only
    id: int

    class Config:
        orm_mode = True


# Line
class LineBase(BaseModel):  # read and create
    name: str
    section_code: str
    wc_code: str
    part_id: int


class LineCreate(LineBase):  # create only
    pass


class Line(LineBase):  # read only
    id: int

    class Config:
        orm_mode = True


# Machine
class MachineBase(BaseModel):  # read and create
    name: str
    machine_index: int
    line_id: int


class MachineCreate(MachineBase):  # create only
    pass


class Machine(MachineBase):  # read only
    id: int

    class Config:
        orm_mode = True
