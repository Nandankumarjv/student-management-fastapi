# Student Management API

A RESTful Student Management API built using **FastAPI, SQLAlchemy, and PostgreSQL**.

## Features

- Create a student
- Get all students
- Get a student by ID
- Update a student
- Delete a student
- Request validation using Pydantic
- Response validation using Pydantic
- SQLAlchemy ORM
- PostgreSQL database
- Dependency Injection for database sessions
- Exception handling
- HTTP middleware
- Environment variables
- Application logging
- Modular project structure

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn
- Psycopg

## Project Structure

```text
StudentAPI/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   └── main.py
│
├── database/
│   ├── __init__.py
│   └── database.py
│
├── models/
│   ├── __init__.py
│   └── student.py
│
├── routers/
│   ├── __init__.py
│   └── students.py
│
├── schemas/
│   ├── __init__.py
│   └── student.py
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt