from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from services.payment_service import PaymentService
from models.model import SessionLocal
from services.auth_service import get_current_user


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", summary="Process Payment", description="Processes the payment for a specific booking.")
def process_payment(
    user_id: int = Depends(get_current_user), 
    booking_id: int = Form(..., description="The ID of the booking for which the payment is being made."), 
    amount: int = Form(..., description="The payment amount."), 
    db: Session = Depends(get_db)
):
    """
    Process the payment for a specific booking.

    - **user_id**: Extracted from the authorization token of the logged-in user.
    - **booking_id**: The ID of the booking.
    - **amount**: The payment amount.
    """
    try:
        return PaymentService.process_payment(db, user_id, booking_id, amount)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
