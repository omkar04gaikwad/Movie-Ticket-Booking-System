## Overview
We have developed a Kindle Library Management System to help users efficiently manage and organize their book collections. The system allows users to add, update, and categorize books by genre and author, while also tracking reading progress, providing a seamless and user-friendly experience similar to Kindle.

This system is built using Django and follows a microservices architecture, ensuring scalability and modularity. The key services include:
1. Book Service: Manages all book-related operations such as adding, updating, and deleting books. It tracks metadata like titles, authors, genres, and reading status (read, unread, in-progress).
2. User Service: Handles user authentication, registration, and personalized settings, allowing users to maintain their unique library.
3. Search Service: Provides fast search functionality, enabling users to efficiently search their book collections by title, author, or genre.

Each microservice operates independently and communicates via RESTful APIs, providing a flexible and scalable architecture. For asynchronous communication between services, we use RabbitMQ, which ensures that tasks are processed efficiently even under high traffic or large volumes of requests.

For service discovery and dynamic service registration, we utilize Consul. This allows services to automatically register themselves and discover other services without the need for hardcoded connections. With Consul, services can dynamically locate each other, ensuring flexibility and easy scaling as the system grows.

Each microservice operates its own PostgreSQL database, adhering to the Database-per-Service principle, ensuring data integrity and independent scaling of services.

The system is designed to be extendable, allowing for easy future additions such as advanced analytics or real-time engagement tracking.


## Architecture Overview

The Library Management System (LMS) utilizes a microservices architecture where each core function of the application is isolated into separate services. Below is the diagram that illustrates the architecture:

![Architecture Diagram](https://github.com/omkar04gaikwad/Booknest-Library_Management_system/resources/architecture.png)

### System Overview:

- **User Service** acts as the API Gateway, handling user authentication, authorization, and management. It forwards requests to the **Book Service** and **Search Service** using **Consul** for service discovery and dynamic service registration.
- **Book Service** manages all operations related to books, including book details, borrowing, and returning records.
- **Search Service** handles optimized search queries and recommendations, querying an indexed search database for quick results.

### Microservice Design:

- **User Service**: Responsible for managing users (admins and borrowers) and integrating with the **Book Service** for borrowing and returning books.
- **Book Service**: Handles book details, inventory, transactions, and borrowing/returning history.
- **Search Service**: Provides a fast and efficient search mechanism for books based on indexed data and ensures real-time availability updates.

### Database Descriptions:

#### 1. User Service Database:
- **Tables**:
  - `Users`: Contains user information, such as `user_id`, `name`, `email`, `password`, and `role`.
  - `Admin Accounts`: Stores information specific to admin users.
  - `Borrowers`: Contains borrower details, including `borrower_id`, `user_id`, `account details`.
  
  **Relationships**:
  - The `Users` table is linked with the `Borrowers` table via `user_id` to differentiate between admins and borrowers.

#### 2. Book Service Database:
- **Tables**:
  - `Books`: Stores book metadata such as `book_id`, `title`, `author`, `ISBN`, `available_copies`, etc.
  - `Transactions`: Keeps a record of all book borrowings, including `transaction_id`, `borrower_id`, `book_id`, `borrow_date`, and `return_date`.
  - `History`: Logs all borrowing history for reporting purposes.

  **Relationships**:
  - The `Books` table connects with the `Transactions` table through `book_id`, to track borrow and return activities.

#### 3. Search Service Database:
- **Tables**:
  - `Search Index`: Indexes book details for efficient searching by `title`, `author`, `category`, etc.
  - `Borrow History`: Logs user searches and borrow history for future suggestions and analytics.

  **Relationships**:
  - The `Search Index` table links with the `Books` table in the **Book Service Database** to keep search results up-to-date with real-time book availability.

This setup allows for a scalable, flexible architecture with a distributed microservices approach, ensuring that each service operates independently while working together to deliver a cohesive system for library management.
