# app/schemas/training.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TrainingBase(BaseModel):
    name: str
    institution: str
    training_date: datetime
    certificate_url: Optional[str] = None
    duration: Optional[str] = None

class TrainingCreate(TrainingBase):
    pass

class Training(TrainingBase):
    id: int
    
    class Config:
        from_attributes = True