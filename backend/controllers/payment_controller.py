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

@router.post("/")
def process_payment(
    user_id: int = Depends(get_current_user), 
    booking_id: int = Form(...), 
    amount: int = Form(...), 
    db: Session = Depends(get_db)
):
    try:
        return PaymentService.process_payment(db, user_id, booking_id, amount)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
