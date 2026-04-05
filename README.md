# Table Tennis Simulator

## Description
This project is a Table Tennis Simulator, inspired by games like Brasfoot and Cockpit Manager 14, but focused on table tennis. It allows users to manage athletes (players) with attributes such as attack, defense, and serve (ranging from 0 to 20), and simulate matches between them. The project was originally developed as a CLI application and has been migrated to a web API using FastAPI.

The application provides a RESTful API for:
- Creating, reading, updating, and deleting athletes.
- Simulating table tennis matches based on athlete stats, including point-by-point calculations, game wins, and overall match results.

Technologies used:
- **Python**: Main programming language.
- **FastAPI**: Framework for building the web API.
- **MongoDB**: NoSQL database for storing athlete data.
- **Docker**: Containerization for MongoDB.
- **Pydantic**: For data validation and schemas.
- **Pandas & Tabulate**: For displaying scoreboards (used in utilities, though primarily for CLI).

The simulation engine calculates match outcomes probabilistically based on athlete attributes, considering factors like serve accuracy, attack/defense balance, and random variations.

## Code Structure
The project is organized as follows:

- **main.py**: Entry point for the FastAPI application, including lifespan management for database initialization.
- **routers/**: Contains API route handlers.
  - **athlete_router.py**: Routes for athlete CRUD operations (GET, POST, PUT, DELETE).
  - **simulation_router.py**: Route for simulating matches between two athletes.
- **services/**: Business logic layer.
  - **athlete_service.py**: Handles athlete operations, including formatting and error handling.
- **repositories/**: Data access layer.
  - **athletes_repository.py**: MongoDB operations for athletes (create, read, update, delete).
- **schemas/**: Data models.
  - **athlete_schema.py**: Pydantic model for Athlete with validation for stats (0-20).
- **core/**: Core logic.
  - **match_engine.py**: Simulation engine for table tennis matches, including point calculation, service rotation, and win conditions.
- **database/**: Database configuration.
  - **mongo.py**: MongoDB client setup.
  - **init_mongo.py**: Database initialization, including index creation and seeding with sample athletes.
- **utils/**: Utility functions.
  - **utils.py**: Functions for displaying scoreboards, user input validation, and screen clearing.
- **docker/**: Docker configuration.
  - **docker-compose.yml**: Sets up MongoDB container with volume persistence.
- **requirements.txt**: List of Python dependencies (e.g., fastapi, pymongo, pydantic, pandas, tabulate).
- **README.md**: This file.

## Prerequisites
- Python 3.8 or higher.
- Docker and Docker Compose (for running MongoDB).
- Operating system: Windows (commands provided for CMD).

## Step-by-Step to Run the Code via CMD
1. Clone the repository:
   ```
   git clone https://github.com/Calixtoyago/Table-Tennis-Simulator.git
   ```
2. Open the Command Prompt (CMD) on Windows. You can do this by pressing `Win + R`, typing `cmd`, and pressing Enter.
3. Navigate to the project folder:
   ```
   cd Table-Tennis-Simulator
   ```
4. Install Python dependencies:
   ```
   pip install -r requirements/requirements.txt
   ```
5. Start MongoDB using Docker Compose (ensure Docker is running):
   ```
   docker-compose -f docker/docker-compose.yml up -d
   ```
   This will start MongoDB on port 27018 (mapped from container's 27017).
6. Run the FastAPI application:
   ```
   uvicorn main:app --reload
   ```
   The server will start, typically on http://127.0.0.1:8000. You can access the API documentation at http://127.0.0.1:8000/docs (Swagger UI).
7. (Optional) To run tests, if any are added in the future:
   ```
   python -m pytest tests/
   ```

To stop MongoDB:
```
docker-compose -f docker/docker-compose.yml down
```

If the project uses a web server, access it in the browser after execution (e.g., http://127.0.0.1:8000). In case of errors, check the logs in CMD or the FastAPI output.

For more details, contact the developer.