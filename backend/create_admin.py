# create_admin.py

from app.auth.hashing import Hash
from app.models.admin import Admin
from app.database import SessionLocal

def create_admin():
    db = SessionLocal()

    email = "admin@example.com"
    password = "admin123"

    # Avoid duplicate creation
    existing_admin = db.query(Admin).filter(Admin.email == email).first()
    if existing_admin:
        print("Admin already exists.")
        return

    hashed_pw = Hash.get_password_hash(password)
    admin = Admin(email=email, password=hashed_pw)
    db.add(admin)
    db.commit()
    db.refresh(admin)

    print(f"Admin created: {admin.email}")

if __name__ == "__main__":
    create_admin()
