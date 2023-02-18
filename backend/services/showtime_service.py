from sqlalchemy.orm import Session
from models.model import Showtime, Seat

class ShowtimeService:
    @staticmethod
    def get_showtimes_by_movie(db_session: Session, movie_name: str):
        # Fetch showtimes for a specific movie
        return db_session.query(Showtime).filter(Showtime.movie_name == movie_name).all()

    @staticmethod
    def get_showtimes_by_city(db_session: Session, city: str):
        # Fetch showtimes for a specific city
        return db_session.query(Showtime).filter(Showtime.city == city).all()
    
    @staticmethod
    def get_showtimes_by_movie_and_city(db_session: Session, movie_name: str, city: str):
        results = db_session.query(Showtime).filter(
            Showtime.movie_name == movie_name, 
            Showtime.city == city
        ).all()
        
        if not results:
            raise Exception(f"No showtimes found for movie '{movie_name}' in city '{city}'")
        
        return results
    
    @staticmethod
    def get_showtimes_all(db_session: Session):
        # Fetch showtimes for a specific city
        return db_session.query(Showtime).all()

    @staticmethod
    def get_seat_availability(db_session: Session, showtime_id: int):
        # Fetch seat availability for a specific showtime
        seats = db_session.query(Seat).filter(Seat.showtime_id == showtime_id).all()
        return [{"seat_number": seat.seat_number, "status": seat.status} for seat in seats]
