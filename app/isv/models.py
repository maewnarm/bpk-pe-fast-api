from sqlalchemy import Boolean, Column, Integer, String, Time, Date, ForeignKey
from sqlalchemy.orm import relationship
# from sqlalchemy_utils import ChoiceType

from ..database import Base

class Operation_record(Base):
    __tablename__ = "operation_record"

    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(Integer, ForeignKey("machine.id"))
    _date = Column(Date)
    _time = Column(Time)
    signal = Column(Integer)
    detail = Column(String)
    
    # machine = relationship("Machine", back_populates="record")
