from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
from models.model import User, SessionLocal

def get_current_user(authorization: str = Header(None)):
    """
    Extracts the user_id from the Authorization token.
    Assumes a simple token-based authentication where the token is the user_id.
    """
    print(f"Received Authorization Header: {authorization}")  # Debugging
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header missing!")
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format. Use 'Bearer <token>'")

    try:
        token = authorization.split("Bearer ")[1]  # Extract token
        user_id = int(token)  # Convert token to user_id (assuming simple integer tokens)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Check if user exists
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user_id  # Return the authenticated user ID
