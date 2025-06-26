# app/models/employee_project_skill.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class EmployeeProjectSkill(Base):
    __tablename__ = "employee_project_skills"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    skill_id = Column(Integer, ForeignKey("employee_skills.id"))
    employee_project_id = Column(Integer, ForeignKey("employee_projects.id"))
    
    # Relationships
    employee_project = relationship("EmployeeProject", back_populates="employee_project_skills")