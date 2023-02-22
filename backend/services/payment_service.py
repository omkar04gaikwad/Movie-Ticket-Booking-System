from sqlalchemy.orm import Session
from models.model import Payment, Booking, Seat
from datetime import datetime
class PaymentService:
    @staticmethod
    def process_payment(db_session: Session, user_id: int, booking_id: int, amount: int):
        # Ensure booking exists and belongs to the user
        booking = db_session.query(Booking).filter(Booking.id == booking_id, Booking.user_id == user_id).first()
        if not booking:
            raise Exception("Booking not found or unauthorized!")

        # Create payment record
        payment = Payment(user_id=user_id, booking_id=booking_id, amount=amount, status="success")
        db_session.add(payment)
        db_session.commit()

        return {"message": "Payment successful!", "payment_id": payment.id}