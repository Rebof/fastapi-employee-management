# app/crud/employee_skill.py
from sqlalchemy.orm import Session
from app.models.employee_skill import EmployeeSkill
from app.schemas.employee_skill import EmployeeSkillCreate

def get_skill(db: Session, skill_id: int):
    return db.query(EmployeeSkill).filter(EmployeeSkill.id == skill_id).first()

def get_skills(db: Session, skip: int = 0, limit: int = 100):
    return db.query(EmployeeSkill).offset(skip).limit(limit).all()

def create_skill(db: Session, skill: EmployeeSkillCreate):
    db_skill = EmployeeSkill(**skill.dict())
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

def update_skill(db: Session, skill_id: int, skill: EmployeeSkillCreate):
    db_skill = db.query(EmployeeSkill).filter(EmployeeSkill.id == skill_id).first()
    if db_skill:
        for key, value in skill.dict().items():
            setattr(db_skill, key, value)
        db.commit()
        db.refresh(db_skill)
    return db_skill

def delete_skill(db: Session, skill_id: int):
    db_skill = db.query(EmployeeSkill).filter(EmployeeSkill.id == skill_id).first()
    if db_skill:
        db.delete(db_skill)
        db.commit()
    return db_skill
