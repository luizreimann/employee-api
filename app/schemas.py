from pydantic import BaseModel
from datetime import date

class EmployeeBase(BaseModel):
    name: str
    cpf: str
    rg: str
    birth_date: date
    address: str
    marital_status: str
    position: str
    hiring_date: date

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int
    class Config:
        orm_mode = True