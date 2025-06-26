# app/routers/project.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.project import Project, ProjectCreate
from app.crud import project as crud_project

router = APIRouter()

@router.post("/", response_model=Project)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    return crud_project.create_project(db=db, project=project)

@router.get("/", response_model=List[Project])
def read_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    projects = crud_project.get_projects(db, skip=skip, limit=limit)
    return projects

@router.get("/{project_id}", response_model=Project)
def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud_project.get_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@router.put("/{project_id}", response_model=Project)
def update_project(project_id: int, project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = crud_project.update_project(db, project_id=project_id, project=project)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud_project.delete_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": "Project deleted successfully"}