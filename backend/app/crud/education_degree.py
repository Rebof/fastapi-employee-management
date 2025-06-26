# app/crud/education_degree.py
from sqlalchemy.orm import Session
from app.models.education_degree import EducationDegree
from app.schemas.education_degree import EducationDegreeCreate


def get_degree(db: Session, degree_id: int):
    return db.query(EducationDegree).filter(EducationDegree.id == degree_id).first()


def get_degrees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(EducationDegree).offset(skip).limit(limit).all()


def create_degree(db: Session, degree: EducationDegreeCreate):
    db_degree = EducationDegree(**degree.dict())
    db.add(db_degree)
    db.commit()
    db.refresh(db_degree)
    return db_degree


def update_degree(db: Session, degree_id: int, degree: EducationDegreeCreate):
    db_degree = db.query(EducationDegree).filter(EducationDegree.id == degree_id).first()
    if db_degree:
        for key, value in degree.dict().items():
            setattr(db_degree, key, value)
        db.commit()
        db.refresh(db_degree)
    return db_degree


def delete_degree(db: Session, degree_id: int):
    db_degree = db.query(EducationDegree).filter(EducationDegree.id == degree_id).first()
    if db_degree:
        db.delete(db_degree)
        db.commit()
    return db_degree