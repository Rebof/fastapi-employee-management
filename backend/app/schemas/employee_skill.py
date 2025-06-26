# app/schemas/employee_skill.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EmployeeSkillBase(BaseModel):
    skill_name: str
    last_used: Optional[datetime] = None
    experience: Optional[str] = None

class EmployeeSkillCreate(EmployeeSkillBase):
    pass

class EmployeeSkill(EmployeeSkillBase):
    id: int
    
    class Config:
        from_attributes = True