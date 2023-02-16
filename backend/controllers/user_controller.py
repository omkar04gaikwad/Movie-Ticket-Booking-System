from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from services.user_service import UserService
from models.model import SessionLocal  # Corrected import

router = APIRouter()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register_user(
    name: str = Form(...),  # Expect name as a form field
    email: str = Form(...),  # Expect email as a form field
    password: str = Form(...),  # Expect password as a form field
    db: Session = Depends(get_db)
):
    try:
        return UserService.register_user(db, name, email, password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login_user(
    email: str = Form(...),  # Expect email as a form field
    password: str = Form(...),  # Expect password as a form field
    db: Session = Depends(get_db)
):
    try:
        return UserService.login_user(db, email, password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))