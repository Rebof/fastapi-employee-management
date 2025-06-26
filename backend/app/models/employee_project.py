# app/models/employee_project.py
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class EmployeeProject(Base):
    __tablename__ = "employee_projects"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    
    # Relationships
    employee = relationship("Employee", back_populates="employee_projects")
    project = relationship("Project", back_populates="employee_projects")
    employee_project_skills = relationship("EmployeeProjectSkill", back_populates="employee_project")