from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import pandas as pd
from datetime import datetime, timedelta
import random

# Define the SQLite database file
DATABASE_URL = "sqlite:///movie_booking.db"

# Create the engine and base
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

# Define the Users table
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

# Define the Showtimes table
class Showtime(Base):
    __tablename__ = 'showtimes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    movie_name = Column(String, nullable=False)
    theater_name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    show_date = Column(DateTime, nullable=False)
    show_time = Column(String, nullable=False)

# Define the Seats table
class Seat(Base):
    __tablename__ = 'seats'

    id = Column(Integer, primary_key=True, autoincrement=True)
    showtime_id = Column(Integer, ForeignKey('showtimes.id'), nullable=False)
    seat_number = Column(String, nullable=False)
    status = Column(Boolean, default=True)  # True = Available, False = Booked

    showtime = relationship("Showtime", back_populates="seats")

# Define the Bookings table
class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    showtime_id = Column(Integer, ForeignKey('showtimes.id'), nullable=False)
    seat_id = Column(Integer, ForeignKey('seats.id'), nullable=False)
    booking_time = Column(DateTime, nullable=False)

    user = relationship("User")
    showtime = relationship("Showtime")
    seat = relationship("Seat")

# Relationships for foreign key linking
Showtime.seats = relationship("Seat", back_populates="showtime")

# Create all tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

print("Database and tables created successfully!")

# Populate Users table
users = [
    User(name="John Doe", email="john@example.com", password="password123"),
    User(name="Jane Smith", email="jane@example.com", password="securepass"),
    User(name="Bob Johnson", email="bob@example.com", password="mypassword")
]
session.add_all(users)
session.commit()
print("Users table populated.")

# Load Kaggle CSV data
movies_csv = "tmdb_5000_movies.csv"  # Replace with the actual path to your CSV file
movies_df = pd.read_csv(movies_csv)

# Populate Showtimes table based on movies CSV
showtimes = []
theater_names = [
    "AMC Boston Common", "Regal Fenway", "Cinemark NYC", 
    "ArcLight Chicago", "Alamo Drafthouse LA"
]
cities = ["Boston", "NYC", "Chicago", "Los Angeles", "San Francisco"]

for _, row in movies_df.iterrows():
    movie_name = row["title"]
    for _ in range(3):  # Generate 3 showtimes per movie
        showtime = Showtime(
            movie_name=movie_name,
            theater_name=random.choice(theater_names),
            city=random.choice(cities),
            show_date=datetime.now() + timedelta(days=random.randint(1, 30)),
            show_time=f"{random.randint(10, 22)}:00"
        )
        showtimes.append(showtime)

session.add_all(showtimes)
session.commit()
print("Showtimes table populated.")

# Populate Seats table for each showtime
seats = []
for showtime in session.query(Showtime).all():
    for i in range(1, 21):  # Assume 20 seats per showtime
        seat = Seat(
            showtime_id=showtime.id,
            seat_number=f"A{i}",
            status=True
        )
        seats.append(seat)

session.add_all(seats)
session.commit()
print("Seats table populated.")
