# app/models/education_degree.py
from sqlalchemy import Column, Integer, String
from app.database import Base

class EducationDegree(Base):
    __tablename__ = "education_degrees"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)  # e.g., "Bachelor's", "Master's", "PhD"