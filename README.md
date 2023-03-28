# Movie Booking App

## Overview
The Movie Booking App is designed to allow users to search for movies, book tickets, and manage bookings through an interactive interface. The application also provides admin capabilities to manage movie listings and update ticket statuses.

### Features
1. **User Registration and Login**:
   - Users can register and log in.
   - Password reset functionality is available.
2. **Browse and Search Movies**:
   - View all released movies.
   - Search movies by name.
3. **Book Tickets**:
   - Users can book tickets for movies.
   - Track seat numbers and ticket availability.
4. **Admin Management**:
   - Admins can update ticket availability.
   - View the status of booked tickets.

---

## Application Architecture


The architecture includes components for REST API development, messaging, monitoring, and database integration. It follows a modular approach, ensuring scalability and maintainability.

---

## Cloud Architecture


The application is deployed on AWS, leveraging services like AWS Lambda, API Gateway, DynamoDB, and Elastic Load Balancer for high availability and performance.

---

## Toolchain

### Competencies and Tools Used
- **Programming**: Java (Spring Boot)
- **Frontend**: Angular or React
- **Messaging**: Kafka
- **Database**: MongoDB, Cassandra, or Redis
- **Monitoring**: Prometheus and Grafana
- **Containerization**: Docker
- **Version Control**: Git
- **Testing**: JUnit, Mockito
- **Build Tool**: Maven

---

## Development Flow

### User Stories

#### **US_01: Registration and Login**
- Users can register with mandatory details.
- Users can log in, reset passwords, and log out.

#### **US_02: View & Search Movies**
- Users can browse all movies.
- Search for movies by name.

#### **US_03: Book Tickets**
- Users can book tickets, specifying movie name, theatre name, and seat details.

#### **US_04: Admin Management**
- Admins can view booked tickets.
- Update ticket availability and status (e.g., "SOLD OUT" or "BOOK ASAP").

---

## Expected Deliverables

### Backend
1. REST APIs:
   - **Register**: `/api/v1.0/moviebooking/register`
   - **Login**: `/api/v1.0/moviebooking/login`
   - **Search Movies**: `/api/v1.0/moviebooking/movies/search/{movieName}`
   - **Book Tickets**: `/api/v1.0/moviebooking/{movieName}/book`
   - **Admin Actions**: `/api/v1.0/moviebooking/admin/addmovie`

2. **Database**:
   - Use MongoDB with Spring Data for ORM.
   - Custom queries for complex operations.

3. **Messaging**:
   - Kafka for inter-service communication.

4. **Logging and Monitoring**:
   - Logstash for centralized logging.
   - Prometheus and Grafana for monitoring metrics.

---

## Frontend
1. Developed using Angular or React.
2. Validations for all input fields.
3. Follows proper naming conventions and SOLID design principles.

---

## Deployment

### Backend
- Use AWS ECS for container management.
- Deploy backend services using AWS Lambda and API Gateway.

### Frontend
- Host frontend artifacts in an S3 bucket.
- Use Amazon Route 53 for domain management.

---

## Methodology
- Agile development methodology.
- Continuous Integration and Continuous Deployment (CI/CD).



---
