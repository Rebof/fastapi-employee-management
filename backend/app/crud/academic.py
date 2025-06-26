# app/crud/academic.py
from sqlalchemy.orm import Session
from app.models.academic import Academic
from app.schemas.academic import AcademicCreate

def get_academic(db: Session, academic_id: int):
    return db.query(Academic).filter(Academic.id == academic_id).first()

def get_academics(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Academic).offset(skip).limit(limit).all()

def get_academics_by_employee(db: Session, employee_id: int):
    return db.query(Academic).filter(Academic.employee_id == employee_id).all()

def create_academic(db: Session, academic: AcademicCreate):
    db_academic = Academic(**academic.dict())
    db.add(db_academic)
    db.commit()
    db.refresh(db_academic)
    return db_academic

def update_academic(db: Session, academic_id: int, academic: AcademicCreate):
    db_academic = db.query(Academic).filter(Academic.id == academic_id).first()
    if db_academic:
        for key, value in academic.dict().items():
            setattr(db_academic, key, value)
        db.commit()
        db.refresh(db_academic)
    return db_academic

def delete_academic(db: Session, academic_id: int):
    db_academic = db.query(Academic).filter(Academic.id == academic_id).first()
    if db_academic:
        db.delete(db_academic)
        db.commit()
    return db_academic

