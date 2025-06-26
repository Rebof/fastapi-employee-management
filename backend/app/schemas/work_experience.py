
# app/schemas/work_experience.py
from pydantic import BaseModel

class WorkExperienceBase(BaseModel):
    company_name: str
    job_title: str
    date_range: str
    employee_id: int

class WorkExperienceCreate(WorkExperienceBase):
    pass

class WorkExperience(WorkExperienceBase):
    id: int
    
    class Config:
        from_attributes = True