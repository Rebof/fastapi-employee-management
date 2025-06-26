# app/routers/education_degree.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.education_degree import EducationDegree, EducationDegreeCreate
from app.crud import education_degree as crud_degree

router = APIRouter()

@router.post("/", response_model=EducationDegree)
def create_degree(degree: EducationDegreeCreate, db: Session = Depends(get_db)):
    return crud_degree.create_degree(db=db, degree=degree)


@router.get("/", response_model=List[EducationDegree])
def read_degrees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_degree.get_degrees(db, skip=skip, limit=limit)


@router.get("/{degree_id}", response_model=EducationDegree)
def read_degree(degree_id: int, db: Session = Depends(get_db)):
    db_degree = crud_degree.get_degree(db, degree_id=degree_id)
    if db_degree is None:
        raise HTTPException(status_code=404, detail="Degree not found")
    return db_degree


@router.put("/{degree_id}", response_model=EducationDegree)
def update_degree(degree_id: int, degree: EducationDegreeCreate, db: Session = Depends(get_db)):
    db_degree = crud_degree.update_degree(db, degree_id=degree_id, degree=degree)
    if db_degree is None:
        raise HTTPException(status_code=404, detail="Degree not found")
    return db_degree


@router.delete("/{degree_id}")
def delete_degree(degree_id: int, db: Session = Depends(get_db)):
    db_degree = crud_degree.delete_degree(db, degree_id=degree_id)
    if db_degree is None:
        raise HTTPException(status_code=404, detail="Degree not found")
    return {"message": "Degree deleted successfully"}