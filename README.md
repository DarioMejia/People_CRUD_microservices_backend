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
Each service in this microservices architecture exposes specific endpoints for CRUD operations. Below are the endpoints and their corresponding functionalities:
1. **Create Service (Port 8011)**
   - POST `localhost:8011/`: Create a new person record.
2. **Read Service (Port 8012)**
   - GET `localhost:8012/`: List all people records.
   - GET `localhost:8012/{doc_id}`: Retrieve details of a specific person record by document ID.
3. **Update Service (Port 8013)**
   - PATCH `localhost:8013/{doc_id}`: Update an existing person record by document ID.
   - PATCH `localhost:8013/{doc_id}/image`: Update the image of a specific person record by document ID.
4. **Delete Service (Port 8014)**
   - DELETE `localhost:8014/{doc_id}`: Delete a specific person record by document ID.
