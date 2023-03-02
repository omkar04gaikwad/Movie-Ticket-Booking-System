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

@router.get("/", summary="Get Showtimes", description="Fetch showtimes based on movie name, city, or both. If no filter is provided, return all showtimes.")
def get_showtimes(movie_name: str = None, city: str = None, db: Session = Depends(get_db)):
    """
    Fetch showtimes.

    - **movie_name**: (Optional) The name of the movie to filter showtimes.
    - **city**: (Optional) The city to filter showtimes.

    Returns:
    - Showtimes filtered by the provided parameters or all showtimes if no filter is provided.
    """
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

@router.get("/{showtime_id}/seats", summary="Get Seat Availability", description="Fetch seat availability for a specific showtime.")
def get_seat_availability(showtime_id: int, db: Session = Depends(get_db)):
    """
    Fetch seat availability for a given showtime.

    - **showtime_id**: The ID of the showtime for which seat availability is requested.

    Returns:
    - A list of available and booked seats for the specified showtime.
    """
    try:
        return ShowtimeService.get_seat_availability(db, showtime_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
