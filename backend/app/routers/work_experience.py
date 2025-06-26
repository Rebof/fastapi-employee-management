# app/routers/work_experience.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.work_experience import WorkExperience, WorkExperienceCreate
from app.crud import work_experience as crud_work_exp

router = APIRouter()

@router.post("/", response_model=WorkExperience)
def create_work_experience(work_exp: WorkExperienceCreate, db: Session = Depends(get_db)):
    return crud_work_exp.create_work_experience(db=db, work_exp=work_exp)

@router.get("/", response_model=List[WorkExperience])
def read_work_experiences(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    work_experiences = crud_work_exp.get_work_experiences(db, skip=skip, limit=limit)
    return work_experiences

@router.get("/employee/{employee_id}", response_model=List[WorkExperience])
def read_work_experiences_by_employee(employee_id: int, db: Session = Depends(get_db)):
    work_experiences = crud_work_exp.get_work_experiences_by_employee(db, employee_id=employee_id)
    return work_experiences

@router.get("/{work_exp_id}", response_model=WorkExperience)
def read_work_experience(work_exp_id: int, db: Session = Depends(get_db)):
    db_work_exp = crud_work_exp.get_work_experience(db, work_exp_id=work_exp_id)
    if db_work_exp is None:
        raise HTTPException(status_code=404, detail="Work experience not found")
    return db_work_exp

@router.put("/{work_exp_id}", response_model=WorkExperience)
def update_work_experience(work_exp_id: int, work_exp: WorkExperienceCreate, db: Session = Depends(get_db)):
    db_work_exp = crud_work_exp.update_work_experience(db, work_exp_id=work_exp_id, work_exp=work_exp)
    if db_work_exp is None:
        raise HTTPException(status_code=404, detail="Work experience not found")
    return db_work_exp

@router.delete("/{work_exp_id}")
def delete_work_experience(work_exp_id: int, db: Session = Depends(get_db)):
    db_work_exp = crud_work_exp.delete_work_experience(db, work_exp_id=work_exp_id)
    if db_work_exp is None:
        raise HTTPException(status_code=404, detail="Work experience not found")
    return {"message": "Work experience deleted successfully"}