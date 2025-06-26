# app/schemas/employee_project_skill.py
from pydantic import BaseModel

class EmployeeProjectSkillBase(BaseModel):
    employee_id: int
    skill_id: int
    employee_project_id: int

class EmployeeProjectSkillCreate(EmployeeProjectSkillBase):
    pass

class EmployeeProjectSkill(EmployeeProjectSkillBase):
    id: int
    
    class Config:
        from_attributes = True