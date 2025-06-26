# app/schemas/project.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    start_date: datetime
    end_date: Optional[datetime] = None

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    
    class Config:
        from_attributes = True