# app/schemas/__init__.py
from .employee import Employee, EmployeeCreate
from .employee_skill import EmployeeSkill, EmployeeSkillCreate
from .employee_skilllevel import EmployeeSkillLevel, EmployeeSkillLevelCreate
from .academic import Academic, AcademicCreate
from .education_degree import EducationDegree, EducationDegreeCreate
from .work_experience import WorkExperience, WorkExperienceCreate
from .project import Project, ProjectCreate
from .training import Training, TrainingCreate
from .employee_project import EmployeeProject, EmployeeProjectCreate
from .employee_project_skill import EmployeeProjectSkill, EmployeeProjectSkillCreate