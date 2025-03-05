from sqlalchemy import Column, Integer, String, Date, DateTime, Enum
from sqlalchemy.sql import func
from app.database import Base

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    rg = Column(String, unique=True, nullable=False)
    birth_date = Column(Date, nullable=False)
    address = Column(String, nullable=False)
    marital_status = Column(String, nullable=False)
    position = Column(String, nullable=False)
    hiring_date = Column(Date, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())