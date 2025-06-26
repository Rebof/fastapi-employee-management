# Create main project folders
mkdir -p backend
mkdir -p backend/app
mkdir -p backend/app/models
mkdir -p backend/app/schemas
mkdir -p backend/app/routers
mkdir -p backend/app/crud
mkdir -p backend/app/auth
mkdir -p backend/app/utils

# Create environment and meta files
touch backend/.env
touch backend/requirements.txt
touch backend/README.md
touch backend/.gitignore

# Core app files
touch backend/app/__init__.py
touch backend/app/main.py
touch backend/app/config.py
touch backend/app/database.py

# Models
touch backend/app/models/__init__.py
touch backend/app/models/employee.py
touch backend/app/models/employee_skill.py
touch backend/app/models/employee_skilllevel.py
touch backend/app/models/academic.py
touch backend/app/models/education_degree.py
touch backend/app/models/work_experience.py
touch backend/app/models/project.py
touch backend/app/models/training.py
touch backend/app/models/employee_project.py
touch backend/app/models/employee_project_skill.py

# Schemas
touch backend/app/schemas/__init__.py
touch backend/app/schemas/employee.py
touch backend/app/schemas/employee_skill.py
touch backend/app/schemas/employee_skilllevel.py
touch backend/app/schemas/academic.py
touch backend/app/schemas/education_degree.py
touch backend/app/schemas/work_experience.py
touch backend/app/schemas/project.py
touch backend/app/schemas/training.py
touch backend/app/schemas/employee_project.py
touch backend/app/schemas/employee_project_skill.py

# Routers
touch backend/app/routers/__init__.py
touch backend/app/routers/employee.py
touch backend/app/routers/employee_skill.py
touch backend/app/routers/academic.py
touch backend/app/routers/work_experience.py
touch backend/app/routers/project.py
touch backend/app/routers/training.py

# CRUD
touch backend/app/crud/__init__.py
touch backend/app/crud/employee.py
touch backend/app/crud/employee_skill.py
touch backend/app/crud/employee_skilllevel.py
touch backend/app/crud/academic.py
touch backend/app/crud/education_degree.py
touch backend/app/crud/work_experience.py
touch backend/app/crud/project.py
touch backend/app/crud/training.py
touch backend/app/crud/employee_project.py
touch backend/app/crud/employee_project_skill.py

# Auth
touch backend/app/auth/__init__.py
touch backend/app/auth/hashing.py
touch backend/app/auth/token.py

# Utils
touch backend/app/utils/__init__.py
touch backend/app/utils/helper.py

# Add content to .gitignore
echo "__pycache__/
*.pyc
.env
.env.*
*.sqlite3
.idea/
.vscode/
__pypackages__/
*.log
*.db
/migrations/
.coverage
htmlcov/
dist/
build/
*.egg-info/
" > backend/.gitignore
