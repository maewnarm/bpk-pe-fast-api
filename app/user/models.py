from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    section_code = Column(String, ForeignKey("fast.sections.code"))

    section = relationship("Section", back_populates="users")
    __table_args__ = {'schema':'fast'}


class Section(Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True)
    name = Column(String)
    division = Column(String)

    users = relationship("User", back_populates="section")
    __table_args__ = {'schema':'fast'}
