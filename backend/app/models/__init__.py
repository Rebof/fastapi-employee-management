from app.database import Base

from .academic import Academic
from .education_degree import EducationDegree
from .employee import Employee
from .employee_project import EmployeeProject
from .employee_project_skill import EmployeeProjectSkill
from .employee_skill import EmployeeSkill
from .employee_skilllevel import EmployeeSkillLevel
from .project import Project
from .training import Training
from .work_experience import WorkExperience
from .admin import Admin

__all__ = [
    "Base",
    "Academic",
    "EducationDegree",
    "Employee",
    "EmployeeProject",
    "EmployeeProjectSkill",
    "EmployeeSkill",
    "EmployeeSkillLevel",
    "Project",
    "Training",
    "WorkExperience",
    "Admin",
]
