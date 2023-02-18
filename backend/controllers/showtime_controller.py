from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.showtime_service import ShowtimeService
from models.model import SessionLocal

router = APIRouter()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_showtimes(movie_name: str = None, city: str = None, db: Session = Depends(get_db)):
    try:
        if movie_name and city:
            return ShowtimeService.get_showtimes_by_movie_and_city(db, movie_name, city)
        elif movie_name:
            return ShowtimeService.get_showtimes_by_movie(db, movie_name)
        elif city:
            return ShowtimeService.get_showtimes_by_city(db, city)
        else:
            return ShowtimeService.get_showtimes_all(db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{showtime_id}/seats")
def get_seat_availability(showtime_id: int, db: Session = Depends(get_db)):
    try:
        return ShowtimeService.get_seat_availability(db, showtime_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
