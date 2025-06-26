# app/models/project.py
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(Text)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    
    # Relationships
    employee_projects = relationship("EmployeeProject", back_populates="project")