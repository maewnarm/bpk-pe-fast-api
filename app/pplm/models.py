from sqlalchemy import Boolean, Column, Integer, String, Time, Date, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)


class Part(Base):
    __tablename__ = "part"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"))


class Line(Base):
    __tablename__ = "line"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    section_code = Column(String, nullable=False)
    wc_code = Column(String, nullable=False)
    part_id = Column(Integer, ForeignKey("part.id"))


class Machine(Base):
    __tablename__ = "machine"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    machine_index = Column(Integer, nullable=False)
    line_id = Column(Integer, ForeignKey("line.id"))
    
    # record = relationship("Operation_record", back_populates="machine")
