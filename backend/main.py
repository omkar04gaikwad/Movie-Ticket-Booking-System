from fastapi import FastAPI
from controllers.user_controller import router as user_router
from controllers.showtime_controller import router as showtime_router
from controllers.booking_controller import router as booking_router

# Initialize FastAPI app
app = FastAPI()

# Include user controller routes
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(showtime_router, prefix="/showtimes", tags=["Showtimes"])
app.include_router(booking_router, prefix="/bookings", tags=["Bookings"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Booking System!"}

# To run the application, use the following command:
# uvicorn main:app --reload
