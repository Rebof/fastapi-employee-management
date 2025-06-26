# app/models/employee_skill.py
from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class EmployeeSkill(Base):
    __tablename__ = "employee_skills"
    
    id = Column(Integer, primary_key=True, index=True)
    skill_name = Column(String, index=True)
    last_used = Column(DateTime)
    experience = Column(String)  # Could be years of experience or description

