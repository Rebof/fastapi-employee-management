# app/models/work_experience.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class WorkExperience(Base):
    __tablename__ = "work_experiences"
    
    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String)
    job_title = Column(String)
    date_range = Column(String)  # Could be "2020-2023" or use separate start/end dates
    employee_id = Column(Integer, ForeignKey("employees.id"))
    
    # Relationships
    employee = relationship("Employee", back_populates="work_experiences")