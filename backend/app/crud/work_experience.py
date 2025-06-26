# app/crud/work_experience.py
from sqlalchemy.orm import Session
from app.models.work_experience import WorkExperience
from app.schemas.work_experience import WorkExperienceCreate

def get_work_experience(db: Session, work_exp_id: int):
    return db.query(WorkExperience).filter(WorkExperience.id == work_exp_id).first()

def get_work_experiences(db: Session, skip: int = 0, limit: int = 100):
    return db.query(WorkExperience).offset(skip).limit(limit).all()

def get_work_experiences_by_employee(db: Session, employee_id: int):
    return db.query(WorkExperience).filter(WorkExperience.employee_id == employee_id).all()

def create_work_experience(db: Session, work_exp: WorkExperienceCreate):
    db_work_exp = WorkExperience(**work_exp.dict())
    db.add(db_work_exp)
    db.commit()
    db.refresh(db_work_exp)
    return db_work_exp

def update_work_experience(db: Session, work_exp_id: int, work_exp: WorkExperienceCreate):
    db_work_exp = db.query(WorkExperience).filter(WorkExperience.id == work_exp_id).first()
    if db_work_exp:
        for key, value in work_exp.dict().items():
            setattr(db_work_exp, key, value)
        db.commit()
        db.refresh(db_work_exp)
    return db_work_exp

def delete_work_experience(db: Session, work_exp_id: int):
    db_work_exp = db.query(WorkExperience).filter(WorkExperience.id == work_exp_id).first()
    if db_work_exp:
        db.delete(db_work_exp)
        db.commit()
    return db_work_exp