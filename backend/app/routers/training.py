
# app/routers/training.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.training import Training, TrainingCreate
from app.crud import training as crud_training

router = APIRouter()

@router.post("/", response_model=Training)
def create_training(training: TrainingCreate, db: Session = Depends(get_db)):
    return crud_training.create_training(db=db, training=training)

@router.get("/", response_model=List[Training])
def read_trainings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    trainings = crud_training.get_trainings(db, skip=skip, limit=limit)
    return trainings

@router.get("/{training_id}", response_model=Training)
def read_training(training_id: int, db: Session = Depends(get_db)):
    db_training = crud_training.get_training(db, training_id=training_id)
    if db_training is None:
        raise HTTPException(status_code=404, detail="Training not found")
    return db_training

@router.put("/{training_id}", response_model=Training)
def update_training(training_id: int, training: TrainingCreate, db: Session = Depends(get_db)):
    db_training = crud_training.update_training(db, training_id=training_id, training=training)
    if db_training is None:
        raise HTTPException(status_code=404, detail="Training not found")
    return db_training

@router.delete("/{training_id}")
def delete_training(training_id: int, db: Session = Depends(get_db)):
    db_training = crud_training.delete_training(db, training_id=training_id)
    if db_training is None:
        raise HTTPException(status_code=404, detail="Training not found")
    return {"message": "Training deleted successfully"}
