# Movie Ticket Booking System - Backend

## Overview
This project is a **Movie Ticket Booking System** built using **FastAPI**. It follows a structured **Low-Level Design (LLD)** to ensure modularity, scalability, and maintainability. The system consists of user authentication, showtime management, seat booking, and payment processing.

## Tech Stack
- **Backend**: FastAPI (Python)
- **Database**: SQLite (via SQLAlchemy ORM)
- **Authentication**: Simple Token-based authentication
- **Message Queue**: (Future Expansion - Kafka/RabbitMQ for async processing)
- **Deployment**: (Future Expansion - Docker, AWS)

## System Architecture (Low-Level Design)
```
+--------------------+       +--------------------+       +--------------------+
|   User Service    | ----> | Showtime Service  | ----> |  Booking Service  |
+--------------------+       +--------------------+       +--------------------+
          |                              |                           |
+--------------------+       +--------------------+       +--------------------+
| Auth Middleware  |       | Payment Service  |       | Database (SQLite) |
+--------------------+       +--------------------+       +--------------------+
```

### **Component Breakdown**
1. **User Service**: Handles user registration, login, and authentication.
2. **Showtime Service**: Manages movie schedules and seat availability.
3. **Booking Service**: Handles seat reservation and prevents double bookings.
4. **Payment Service**: Manages payment transactions for successful bookings.
5. **Database (SQLite)**: Stores users, bookings, showtimes, and payments.

---

## **Database Schema**
```
+----------------+        +----------------+        +----------------+        +----------------+
| Users         |        | Showtimes      |        | Seats         |        | Bookings      |
+----------------+        +----------------+        +----------------+        +----------------+
| id (PK)       |        | id (PK)        |        | id (PK)       |        | id (PK)       |
| name          |        | movie_name     |        | showtime_id   |(FK)   | user_id (FK)  |
| email (Unique)|        | theater_name   |        | seat_number   |        | seat_id (FK)  |
| password      |        | city           |        | status (Bool) |        | booking_time  |
+----------------+        +----------------+        +----------------+        +----------------+
```

## **Endpoints Documentation**

### **User Authentication**
- **POST `/users/register`** - Register a new user.
- **POST `/users/login`** - Authenticate user and return token.

### **Showtime Management**
- **GET `/showtimes/`** - Retrieve showtimes by movie or city.
- **GET `/showtimes/{showtime_id}/seats`** - Fetch seat availability for a specific showtime.

### **Booking System**
- **POST `/bookings/`** - Book a seat (Authentication required).
- **GET `/bookings/{user_id}`** - Retrieve all bookings of a user.

### **Payments System**
- **POST `/payments/`** - Process payment for a booking (Authentication required).

---

## **Authentication and Security**
- Uses **Bearer Token Authentication** for user authorization.
- Secure **password hashing** using bcrypt.
- Ensures **role-based access control** for booking and payment services.

---

## **Testing & Documentation**
- **Unit Testing** with `pytest` and `httpx`.
- **Automated API Documentation** with **Swagger UI (`/docs`)** and **ReDoc (`/redoc`)**.

---

## **Setup & Run the Project**
### **1️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
python models/model.py  # Creates tables
uvicorn main:app --reload
pytest
```

