## Overview
We have developed a Kindle Library Management System, a robust platform designed to help users manage their book collections in a seamless and efficient way. This system allows users to add books, organize them by genre and author, and track their reading progress, creating a user experience similar to managing books on Kindle.

The system is built on a microservices architecture using Spring Boot, ensuring that each core functionality is modular and scalable. The primary microservices include:

1. Book Service: Manages book-related operations such as adding, updating, and deleting books. It stores information about titles, authors, genres, and reading statuses (read, unread, in-progress).
2. User Service: Handles user registration, authentication, and personalized book data, allowing users to maintain their own library.
3. Search Service: Provides efficient search functionality, enabling users to search their library by title, author, or genre.
4. Recommendation Service: Offers personalized book suggestions based on user reading history and preferences, enhancing the overall user experience.

Each microservice is developed independently using Spring Boot, ensuring scalability and ease of maintenance. These services communicate via RESTful APIs, ensuring that the frontend interacts with the system in a seamless manner, abstracting the underlying complexity of the microservices architecture.

The Eureka Discovery Server is used for service discovery and inter-service communication. Eureka allows the microservices to dynamically register and communicate with each other without being hard-coded to specific ports or hostnames, ensuring flexibility in deployment.

Data for each service is stored in its own PostgreSQL database following the Database-per-Service pattern. This separation ensures data integrity and allows each service to operate independently while still maintaining communication through APIs.

To ensure portability and isolation, each service is containerized using Docker, which allows the system to be deployed easily in on-premises data centers or multiple environments while maintaining consistency.

## Key Features
1. Microservices Architecture: Independent services for user management, book management, search, and recommendations.
2. RESTful API Communication: Interaction between frontend and backend through REST APIs for seamless user experience.
3. Eureka Discovery: Enables dynamic service registration and discovery, ensuring flexible communication between microservices.
4. PostgreSQL Databases: Each microservice has its own dedicated database for efficient data management.
5. Docker Containerization: Ensures the entire system can be easily deployed and scaled across multiple environments.
6. Scalable and Extensible: The modular architecture allows for easy scaling of individual services and future enhancements like analytics or real-time data processing.