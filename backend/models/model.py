from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from sqlalchemy import create_engine

# Define the SQLite database file (already created)
DATABASE_URL = "sqlite:///movie_booking.db"
engine = create_engine(DATABASE_URL, echo=True)

# Define Base
Base = declarative_base()

# Create session
SessionLocal = sessionmaker(bind=engine)

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

    seats = relationship("Seat", back_populates="showtime")  # One-to-many relationship with seats

# Define the Seats table
class Seat(Base):
    __tablename__ = 'seats'

    id = Column(Integer, primary_key=True, autoincrement=True)
    showtime_id = Column(Integer, ForeignKey('showtimes.id'), nullable=False)
    seat_number = Column(String, nullable=False)
    status = Column(Boolean, default=True)  # True = Available, False = Booked

    showtime = relationship("Showtime", back_populates="seats")  # Belongs to a showtime

# Define the Bookings table
class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    showtime_id = Column(Integer, ForeignKey('showtimes.id'), nullable=False)
    seat_id = Column(Integer, ForeignKey('seats.id'), nullable=False)
    booking_time = Column(DateTime, nullable=False)

    user = relationship("User")  # Belongs to a user
    showtime = relationship("Showtime")  # Belongs to a showtime
    seat = relationship("Seat")  # Belongs to a seat
