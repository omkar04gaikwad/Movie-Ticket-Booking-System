from fastapi import FastAPI
from controllers import user_controller

# Initialize FastAPI app
app = FastAPI()

# Include user controller routes
app.include_router(user_controller.router, prefix="/users", tags=["Users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Booking System!"}

# To run the application, use the following command:
# uvicorn main:app --reload
