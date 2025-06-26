# app/routers/employee_skill.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.employee_skill import EmployeeSkill, EmployeeSkillCreate
from app.crud import employee_skill as crud_skill

router = APIRouter()

@router.post("/", response_model=EmployeeSkill)
def create_skill(skill: EmployeeSkillCreate, db: Session = Depends(get_db)):
    return crud_skill.create_skill(db=db, skill=skill)

@router.get("/", response_model=List[EmployeeSkill])
def read_skills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    skills = crud_skill.get_skills(db, skip=skip, limit=limit)
    return skills

@router.get("/{skill_id}", response_model=EmployeeSkill)
def read_skill(skill_id: int, db: Session = Depends(get_db)):
    db_skill = crud_skill.get_skill(db, skill_id=skill_id)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    return db_skill

@router.put("/{skill_id}", response_model=EmployeeSkill)
def update_skill(skill_id: int, skill: EmployeeSkillCreate, db: Session = Depends(get_db)):
    db_skill = crud_skill.update_skill(db, skill_id=skill_id, skill=skill)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    return db_skill

@router.delete("/{skill_id}")
def delete_skill(skill_id: int, db: Session = Depends(get_db)):
    db_skill = crud_skill.delete_skill(db, skill_id=skill_id)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    return {"message": "Skill deleted successfully"}