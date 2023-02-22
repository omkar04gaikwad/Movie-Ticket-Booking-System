from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from services.booking_service import BookingService
from models.model import SessionLocal
from services.auth_service import get_current_user

router = APIRouter()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def book_seat(
    user_id: int = Depends(get_current_user),
    showtime_id: int = Form(...), 
    seat_number: str = Form(...), 
    db: Session = Depends(get_db)
):
    try:
        return BookingService.book_seat(db, user_id, showtime_id, seat_number)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}")
def get_user_bookings(user_id: int, db: Session = Depends(get_db)):
    try:
        return BookingService.get_user_bookings(db, user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
