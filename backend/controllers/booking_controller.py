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

@router.post("/", summary="Book a Seat", description="Allows a user to book a specific seat for a given showtime.")
def book_seat(
    user_id: int = Depends(get_current_user),
    showtime_id: int = Form(..., description="ID of the showtime for which the seat is being booked."), 
    seat_number: str = Form(..., description="The specific seat number to book."), 
    db: Session = Depends(get_db)
):
    """
    Book a seat for a specific showtime.

    - **user_id**: Extracted from the authorization token of the logged-in user.
    - **showtime_id**: The ID of the showtime.
    - **seat_number**: The seat number to be booked.
    """
    try:
        return BookingService.book_seat(db, user_id, showtime_id, seat_number)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", summary="Get User Bookings", description="Fetch all bookings made by a specific user.")
def get_user_bookings(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all bookings for a user.

    - **user_id**: The ID of the user whose bookings need to be retrieved.
    """
    try:
        return BookingService.get_user_bookings(db, user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
