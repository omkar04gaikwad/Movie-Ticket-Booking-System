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

@router.post("/register", summary="Register a New User", description="Register a new user by providing their name, email, and password.")
def register_user(
    name: str = Form(..., description="The name of the user."),  # Expect name as a form field
    email: str = Form(..., description="The email address of the user."),  # Expect email as a form field
    password: str = Form(..., description="The password for the user."),  # Expect password as a form field
    db: Session = Depends(get_db)
):
    """
    Register a new user.

    - **name**: The name of the user.
    - **email**: The email address of the user.
    - **password**: The password for the user.
    """
    try:
        return UserService.register_user(db, name, email, password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", summary="User Login", description="Authenticate a user by their email and password.")
def login_user(
    email: str = Form(..., description="The email address of the user."),  # Expect email as a form field
    password: str = Form(..., description="The password for the user."),  # Expect password as a form field
    db: Session = Depends(get_db)
):
    """
    Authenticate a user and return a token if valid.

    - **email**: The email address of the user.
    - **password**: The password for the user.
    """
    try:
        return UserService.login_user(db, email, password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
