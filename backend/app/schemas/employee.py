# app/schemas/employee.py
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class EmployeeBase(BaseModel):
    name: str
    email: str

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int
    
    class Config:
        from_attributes = True