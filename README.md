# People_CRUD_microservices_backend

## Overview
This repository implements a backend system for managing people records using microservices architecture. It provides a suite of services for creating, reading, updating, and deleting (CRUD) people records.

## Key Features
- **Microservices Architecture**: Each CRUD operation is handled by a separate microservice, ensuring scalability and maintainability.
- **Data Access Object (DAO) Pattern**: The `PeopleDAO` class in `daos/people_dao.py` abstracts and encapsulates all access to the data source.
- **Data Transfer Object (DTO) Pattern**: The `CreatePeopleDTO`, `DetailPeopleDTO`, and `UpdatePeopleDTO` classes in `dtos/people_dto.py` ensure that data sent over the network is not connected to the database models.
- **Model-View-Controller (MVC) Pattern**: The application is structured into models (data), views (presentation), and controllers (business logic), promoting organized and efficient code.

## Services
1. **Create Service**: Manages the creation of new people records.
2. **Read Service**: Handles fetching details of existing people records.
3. **Update Service**: Allows updating existing people records.
4. **Delete Service**: Facilitates the deletion of people records.

## Technologies Used
- FastAPI
- MongoDB
- Docker
- Cloudinary (for image handling)
 
## Getting Started
To run the application, ensure you have Docker installed and then execute the following command:
```bash
docker-compose up
```
This command will start all the microservices and make them available for use. But, in order to function properly, you should also add a .env files with your personal credentials for MongoDB and Cloudinary.

## Repository Structure
- *daos/:* Contains the Data Access Object for interacting with the database.
- *dtos/:* Includes the Data Transfer Objects used in the application.
- *services/:* Houses the individual microservices for CRUD operations.
- *docker-compose.yml:* Defines the services, networks, and volumes for Docker.

## CRUD Endpoints
The microservices architecture provides distinct services for each CRUD operation. Below are the updated endpoints and their functionalities:
1. **Create Service**
   - POST `/`: Creates a new person record.
     - Endpoint: `http://localhost:8011/`
2. **Read Service**
   - GET `/`: Lists all people records.
     - Endpoint: `http://localhost:8012/`
   - GET `/detail`: Retrieves details of a person by `doc_id` and `doc_type`.
     - Endpoint: `http://localhost:8012/detail?doc_id=<doc_id>&doc_type=<doc_type>`
3. **Update Service**
   - PATCH `/`: Updates a person record by `doc_id` and `doc_type`.
     - Endpoint: `http://localhost:8013/?doc_id=<doc_id>&doc_type=<doc_type>`
4. **Delete Service**
   - DELETE `/`: Deletes a person record by `doc_id` and `doc_type`.
     - Endpoint: `http://localhost:8014/?doc_id=<doc_id>&doc_type=<doc_type>`

Each service is designed to handle specific types of requests, ensuring a clear and efficient architecture for managing people records.

## Service Schemas

Each service in the microservices architecture expects specific data formats for requests and provides responses in defined schemas. Here's a breakdown for each service:


### Create Service (Port 8011)

- **Endpoint**: POST `http://localhost:8011/`
- **Request Schema**:
  - document_type: string
  - document_id: string
  - first_name: string
  - middle_name: string
  - last_name: string
  - birth_date: date
  - gender: string
  - email: string
  - phone: string
  - photo_url: string (Optional)

- **Response Schema**:
  - document_type: string
  - document_id: string
  - first_name: string
  - middle_name: string
  - last_name: string
  - birth_date: date
  - gender: string
  - email: string
  - phone: string
  - photo_url: string

### Read Service (Port 8012)

- **List Endpoint**: GET `http://localhost:8012/`
  - **Response Schema**: Array of people objects as defined in the Create Service response schema.

- **Detail Endpoint**: GET `http://localhost:8012/detail?doc_id=<doc_id>&doc_type=<doc_type>`
  - **Response Schema**: Single person object as defined in the Create Service response schema.

### Update Service (Port 8013)

- **Endpoint**: PATCH `http://localhost:8013/?doc_id=<doc_id>&doc_type=<doc_type>`
- **Request Schema**:
  - first_name: string (optional)
  - last_name: string (optional)
  - age: number (optional)
  - city: string (optional)
  - photo_url: string (optional)

- **Response Schema**: Single person object as defined in the Create Service response schema.

### Delete Service (Port 8014)

- **Endpoint**: DELETE `http://localhost:8014/?doc_id=<doc_id>&doc_type=<doc_type>`
- **Response Schema**:
  - message: string

This document outlines the data formats expected by each service in the microservices architecture for creating, reading, updating, and deleting people records.
