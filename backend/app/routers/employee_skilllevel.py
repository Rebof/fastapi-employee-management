from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.employee_skilllevel import EmployeeSkillLevel, EmployeeSkillLevelCreate
from app.crud import employee_skilllevel as crud_skilllevel

router = APIRouter()

@router.post("/", response_model=EmployeeSkillLevel)
def create_skilllevel(skilllevel: EmployeeSkillLevelCreate, db: Session = Depends(get_db)):
    return crud_skilllevel.create_skilllevel(db=db, skilllevel=skilllevel)

@router.get("/", response_model=List[EmployeeSkillLevel])
def read_skilllevels(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_skilllevel.get_skilllevels(db, skip=skip, limit=limit)

@router.get("/{skilllevel_id}", response_model=EmployeeSkillLevel)
def read_skilllevel(skilllevel_id: int, db: Session = Depends(get_db)):
    db_skilllevel = crud_skilllevel.get_skilllevel(db, skilllevel_id=skilllevel_id)
    if db_skilllevel is None:
        raise HTTPException(status_code=404, detail="Skill level not found")
    return db_skilllevel

@router.put("/{skilllevel_id}", response_model=EmployeeSkillLevel)
def update_skilllevel(skilllevel_id: int, skilllevel: EmployeeSkillLevelCreate, db: Session = Depends(get_db)):
    db_skilllevel = crud_skilllevel.update_skilllevel(db, skilllevel_id=skilllevel_id, skilllevel=skilllevel)
    if db_skilllevel is None:
        raise HTTPException(status_code=404, detail="Skill level not found")
    return db_skilllevel

@router.delete("/{skilllevel_id}")
def delete_skilllevel(skilllevel_id: int, db: Session = Depends(get_db)):
    db_skilllevel = crud_skilllevel.delete_skilllevel(db, skilllevel_id=skilllevel_id)
    if db_skilllevel is None:
        raise HTTPException(status_code=404, detail="Skill level not found")
    return {"message": "Skill level deleted successfully"}
