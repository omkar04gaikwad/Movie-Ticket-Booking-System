from sqlalchemy.orm import Session
from models.model import Booking, Seat
from datetime import datetime

class BookingService:
    @staticmethod
    def book_seat(db_session: Session, user_id: int, showtime_id: int, seat_number: str):
        # Check if the seat is available
        seat = db_session.query(Seat).filter(
            Seat.showtime_id == showtime_id, Seat.seat_number == seat_number, Seat.status == True
        ).first()
        if not seat:
            raise Exception(f"Seat {seat_number} is already booked or does not exist!")

        # Mark seat as booked
        seat.status = False

        # Create booking record
        booking = Booking(user_id=user_id, showtime_id=showtime_id, seat_id=seat.id, booking_time=datetime.now())
        db_session.add(booking)
        db_session.commit()

        return {"message": f"Seat {seat_number} successfully booked!", "booking_id": booking.id }

    @staticmethod
    def get_user_bookings(db_session: Session, user_id: int):
        return db_session.query(Booking).filter(Booking.user_id == user_id).all()
