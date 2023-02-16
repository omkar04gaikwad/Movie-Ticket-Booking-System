from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from models.model import User

class UserService:
    @staticmethod
    def register_user(db_session: Session, name: str, email: str, password: str):
        # Check if the user already exists
        user = db_session.query(User).filter(User.email == email).first()
        if user:
            raise Exception("User already exists!")
        
        # Hash the password
        hashed_password = bcrypt.hash(password)
        
        # Create a new user
        new_user = User(name=name, email=email, password=hashed_password)
        db_session.add(new_user)
        db_session.commit()
        return {"message": "User registered successfully!", "user_id": new_user.id}

    @staticmethod
    def login_user(db_session: Session, email: str, password: str):
        # Fetch user from the database
        user = db_session.query(User).filter(User.email == email).first()
        if not user or not bcrypt.verify(password, user.password):
            raise Exception("Invalid email or password!")
        return {"message": "Login successful!", "user_id": user.id}
