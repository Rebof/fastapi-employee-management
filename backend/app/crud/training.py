# app/crud/training.py
from sqlalchemy.orm import Session
from app.models.training import Training
from app.schemas.training import TrainingCreate

def get_training(db: Session, training_id: int):
    return db.query(Training).filter(Training.id == training_id).first()

def get_trainings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Training).offset(skip).limit(limit).all()

def create_training(db: Session, training: TrainingCreate):
    db_training = Training(**training.dict())
    db.add(db_training)
    db.commit()
    db.refresh(db_training)
    return db_training

def update_training(db: Session, training_id: int, training: TrainingCreate):
    db_training = db.query(Training).filter(Training.id == training_id).first()
    if db_training:
        for key, value in training.dict().items():
            setattr(db_training, key, value)
        db.commit()
        db.refresh(db_training)
    return db_training

def delete_training(db: Session, training_id: int):
    db_training = db.query(Training).filter(Training.id == training_id).first()
    if db_training:
        db.delete(db_training)
        db.commit()
    return db_training