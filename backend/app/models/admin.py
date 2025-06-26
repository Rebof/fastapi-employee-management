
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Admin(Base):
    __tablename__ = "admins"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
