# app/models/academic.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Academic(Base):
    __tablename__ = "academics"
    
    id = Column(Integer, primary_key=True, index=True)
    degree = Column(String)
    institution = Column(String)
    graduation_year = Column(Integer)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    
    # Relationships
    employee = relationship("Employee", back_populates="academics")