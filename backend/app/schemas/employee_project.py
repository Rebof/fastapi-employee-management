# app/schemas/employee_project.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EmployeeProjectBase(BaseModel):
    employee_id: int
    project_id: int
    start_date: datetime
    end_date: Optional[datetime] = None

class EmployeeProjectCreate(EmployeeProjectBase):
    pass

class EmployeeProject(EmployeeProjectBase):
    id: int
    
    class Config:
        from_attributes = True