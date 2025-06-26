

# app/models/employee_skilllevel.py
from sqlalchemy import Column, Integer, String
from app.database import Base

class EmployeeSkillLevel(Base):
    __tablename__ = "employee_skilllevels"
    
    id = Column(Integer, primary_key=True, index=True)
    skill_level = Column(String)  # e.g., "Beginner", "Intermediate", "Advanced", "Expert"    