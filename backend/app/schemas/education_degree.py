# app/schemas/education_degree.py
from pydantic import BaseModel

class EducationDegreeBase(BaseModel):
    name: str

class EducationDegreeCreate(EducationDegreeBase):
    pass

class EducationDegree(EducationDegreeBase):
    id: int
    
    class Config:
        from_attributes = True
