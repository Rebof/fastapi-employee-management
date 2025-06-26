# app/models/training.py
from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class Training(Base):
    __tablename__ = "trainings"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    institution = Column(String)
    training_date = Column(DateTime)
    certificate_url = Column(String)
    duration = Column(String)  # e.g., "40 hours", "2 weeks"