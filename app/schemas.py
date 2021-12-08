from typing import List, Optional

from pydantic import BaseModel

# User
class UserBase(BaseModel):
    employee_id: str
    email: str
    section_code: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


# Section
class SectionBase(BaseModel):
    code: str
    name: str
    division: str


class SectionCreate(SectionBase):
    pass


class Section(SectionBase):
    id: int
    members: List[User] = []

    class Config:
        orm_mode = True
