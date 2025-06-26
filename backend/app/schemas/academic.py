# app/schemas/academic.py
from pydantic import BaseModel

class AcademicBase(BaseModel):
    degree: str
    institution: str
    graduation_year: int
    employee_id: int

class AcademicCreate(AcademicBase):
    pass

class Academic(AcademicBase):
    id: int
    
    class Config:
        from_attributes = True