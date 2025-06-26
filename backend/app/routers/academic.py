# app/routers/academic.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.academic import Academic, AcademicCreate
from app.crud import academic as crud_academic

router = APIRouter()

@router.post("/", response_model=Academic)
def create_academic(academic: AcademicCreate, db: Session = Depends(get_db)):
    return crud_academic.create_academic(db=db, academic=academic)

@router.get("/", response_model=List[Academic])
def read_academics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    academics = crud_academic.get_academics(db, skip=skip, limit=limit)
    return academics

@router.get("/employee/{employee_id}", response_model=List[Academic])
def read_academics_by_employee(employee_id: int, db: Session = Depends(get_db)):
    academics = crud_academic.get_academics_by_employee(db, employee_id=employee_id)
    return academics

@router.get("/{academic_id}", response_model=Academic)
def read_academic(academic_id: int, db: Session = Depends(get_db)):
    db_academic = crud_academic.get_academic(db, academic_id=academic_id)
    if db_academic is None:
        raise HTTPException(status_code=404, detail="Academic record not found")
    return db_academic

@router.put("/{academic_id}", response_model=Academic)
def update_academic(academic_id: int, academic: AcademicCreate, db: Session = Depends(get_db)):
    db_academic = crud_academic.update_academic(db, academic_id=academic_id, academic=academic)
    if db_academic is None:
        raise HTTPException(status_code=404, detail="Academic record not found")
    return db_academic

@router.delete("/{academic_id}")
def delete_academic(academic_id: int, db: Session = Depends(get_db)):
    db_academic = crud_academic.delete_academic(db, academic_id=academic_id)
    if db_academic is None:
        raise HTTPException(status_code=404, detail="Academic record not found")
    return {"message": "Academic record deleted successfully"}