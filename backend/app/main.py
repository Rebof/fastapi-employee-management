from fastapi import FastAPI
from app.database import engine
from app.models import Base  # Import Base from models/__init__.py
from app.routers import (
    employee, 
    employee_skill, 
    academic, 
    project, 
    training,
    work_experience,
    employee_skilllevel,
    auth
)
from fastapi import Depends
from app.auth.oauth2 import get_current_admin
from app.models.admin import Admin

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Management API", version="1.0.0")

# Include routers
app.include_router(auth.router)
app.include_router(employee.router, prefix="/api/v1/employees", tags=["Employees"])
app.include_router(employee_skill.router, prefix="/api/v1/skills", tags=["Skills"])
app.include_router(employee_skilllevel.router, prefix="/skilllevels", tags=["Employee Skill Levels"])

app.include_router(academic.router, prefix="/api/v1/academics", tags=["Academics"])
app.include_router(project.router, prefix="/api/v1/projects", tags=["Projects"])
app.include_router(training.router, prefix="/api/v1/trainings", tags=["Trainings"])
app.include_router(work_experience.router, prefix="/api/v1/work-experience", tags=["Work-Experience"])


@app.get("/")
def root(current_admin: Admin = Depends(get_current_admin)):
    return {"message": f"Welcome, {current_admin.email}. This is the Employee Management API."}