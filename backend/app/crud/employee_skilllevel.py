from sqlalchemy.orm import Session
from app.models.employee_skilllevel import EmployeeSkillLevel
from app.schemas.employee_skilllevel import EmployeeSkillLevelCreate

def get_skilllevel(db: Session, skilllevel_id: int):
    return db.query(EmployeeSkillLevel).filter(EmployeeSkillLevel.id == skilllevel_id).first()

def get_skilllevels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(EmployeeSkillLevel).offset(skip).limit(limit).all()

def create_skilllevel(db: Session, skilllevel: EmployeeSkillLevelCreate):
    db_skilllevel = EmployeeSkillLevel(**skilllevel.dict())
    db.add(db_skilllevel)
    db.commit()
    db.refresh(db_skilllevel)
    return db_skilllevel

def update_skilllevel(db: Session, skilllevel_id: int, skilllevel: EmployeeSkillLevelCreate):
    db_skilllevel = db.query(EmployeeSkillLevel).filter(EmployeeSkillLevel.id == skilllevel_id).first()
    if db_skilllevel:
        for key, value in skilllevel.dict().items():
            setattr(db_skilllevel, key, value)
        db.commit()
        db.refresh(db_skilllevel)
    return db_skilllevel

def delete_skilllevel(db: Session, skilllevel_id: int):
    db_skilllevel = db.query(EmployeeSkillLevel).filter(EmployeeSkillLevel.id == skilllevel_id).first()
    if db_skilllevel:
        db.delete(db_skilllevel)
        db.commit()
    return db_skilllevel
