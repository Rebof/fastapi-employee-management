# app/schemas/employee_skilllevel.py
from pydantic import BaseModel

class EmployeeSkillLevelBase(BaseModel):
    skill_level: str

class EmployeeSkillLevelCreate(EmployeeSkillLevelBase):
    pass

class EmployeeSkillLevel(EmployeeSkillLevelBase):
    id: int
    
    class Config:
        from_attributes = True