from sqlalchemy import Boolean, Column, Integer, String, ForeignKey,DateTime
from sqlalchemy.orm import relationship
# from sqlalchemy_utils import ChoiceType

from ..database import Base

class Operation_record(Base):
    __tablename__ = "operation_record"

    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(Integer, ForeignKey("machines.id"))
    datetime_ = Column(DateTime)
    signal = Column(Integer)
    value = Column(Integer)
    detail = Column(String,default="")
    result = Column(String,default="")
    
    machine = relationship("Machines", back_populates="record")
    # __table_args__ = {'schema': 'fast'}
    
class Machines(Base):
    __tablename__ = "machines"
    
    id = Column(Integer,primary_key=True)
    no = Column(String)
    name = Column(String)
    index = Column(Integer)
    category = Column(String)
    
    record = relationship("Operation_record")
