# FastAPI Employee Management System

A structured FastAPI backend for managing employee information, skills, projects, academics, trainings, and more.

---

## 🚀 Features

- 📋 Employee registration and profile management
- 🧠 Skills & skill levels
- 🎓 Academic history & education degrees
- 💼 Work experience
- 🛠 Projects and employee involvement
- 🏫 Trainings and certifications
- 🔐 Authentication (planned)
- 📦 Modular architecture (models, schemas, routers, CRUD)

---

## 🗂 Project Structure

```
backend/
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── venv/                      # Python virtual environment
└── app/
    ├── main.py               # FastAPI app entry point
    ├── config.py             # Configuration setup
    ├── database.py           # DB engine and session config
    ├── models/               # SQLAlchemy models
    ├── schemas/              # Pydantic schemas
    ├── crud/                 # Business logic
    ├── routers/              # API route handlers
    ├── auth/                 # Token-based auth (planned)
    └── utils/                # Helper utilities
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/fastapi-employee-management.git
cd fastapi-employee-management
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set environment variables
Create a `.env` file in the root directory:
```env
DATABASE_URL=sqlite:///./test.db  # or use PostgreSQL/MySQL connection string
```

### 5. Run the server
```bash
uvicorn app.main:app --reload
```

### 6. **Access the API:**
- API Documentation: http://localhost:8000/docs
- Alternative Docs: http://localhost:8000/redoc
- API Base URL: http://localhost:8000

---

## 🧪 Tech Stack
- **Python 3.10+**
- **FastAPI**
- **SQLAlchemy**
- **Pydantic**
- **SQLite / PostgreSQL** (configurable)

---

## 📚 API Endpoints

### Employees
- `GET /api/v1/employees/` - List all employees
- `POST /api/v1/employees/` - Create new employee
- `GET /api/v1/employees/{id}` - Get employee by ID
- `PUT /api/v1/employees/{id}` - Update employee
- `DELETE /api/v1/employees/{id}` - Delete employee

### Skills
- `GET /api/v1/skills/` - List all skills
- `POST /api/v1/skills/` - Create new skill
- `GET /api/v1/skills/{id}` - Get skill by ID
- `PUT /api/v1/skills/{id}` - Update skill
- `DELETE /api/v1/skills/{id}` - Delete skill

### Academic Records
- `GET /api/v1/academics/` - List all academic records
- `POST /api/v1/academics/` - Create new academic record
- `GET /api/v1/academics/{id}` - Get academic record by ID
- `GET /api/v1/academics/employee/{employee_id}` - Get academics by employee
- `PUT /api/v1/academics/{id}` - Update academic record
- `DELETE /api/v1/academics/{id}` - Delete academic record

### Projects
- `GET /api/v1/projects/` - List all projects
- `POST /api/v1/projects/` - Create new project
- `GET /api/v1/projects/{id}` - Get project by ID
- `PUT /api/v1/projects/{id}` - Update project
- `DELETE /api/v1/projects/{id}` - Delete project

### Work Experience
- `GET /api/v1/work-experience/` - List all work experiences
- `POST /api/v1/work-experience/` - Create new work experience
- `GET /api/v1/work-experience/{id}` - Get work experience by ID
- `GET /api/v1/work-experience/employee/{employee_id}` - Get work experiences by employee
- `PUT /api/v1/work-experience/{id}` - Update work experience
- `DELETE /api/v1/work-experience/{id}` - Delete work experience

### Training
- `GET /api/v1/trainings/` - List all trainings
- `POST /api/v1/trainings/` - Create new training
- `GET /api/v1/trainings/{id}` - Get training by ID
- `PUT /api/v1/trainings/{id}` - Update training
- `DELETE /api/v1/trainings/{id}` - Delete training

---

## 📌 TODO
- Add validations maybe idk

---

## 📄 License
MIT License