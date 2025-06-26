# app/models/employee.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    
    
    # Relationships
    academics = relationship("Academic", back_populates="employee")
    work_experiences = relationship("WorkExperience", back_populates="employee")
    employee_projects = relationship("EmployeeProject", back_populates="employee")
    
