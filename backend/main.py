from fastapi import FastAPI
from controllers.user_controller import router as user_router
from controllers.showtime_controller import router as showtime_router
from controllers.booking_controller import router as booking_router
from controllers.booking_controller import router as booking_router
from controllers.payment_controller import router as payment_router

# Initialize FastAPI app
app = FastAPI(
    title="Movie Ticket Booking System",
    description="A simple API for managing movie ticket bookings, payments, and showtimes.",
    version="1.0.0",
    contact={
        "name": "Omkar Rajendra Gaikwad",
        "email": "omkar04gaikwad@gmail.com"
    }
)


# Include user controller routes
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(showtime_router, prefix="/showtimes", tags=["Showtimes"])
app.include_router(booking_router, prefix="/bookings", tags=["Bookings"])
app.include_router(payment_router, prefix="/payments", tags=["Payments"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Booking System!"}

# To run the application, use the following command:
# uvicorn main:app --reload
