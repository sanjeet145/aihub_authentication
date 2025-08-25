# Auth Service

This service handles authentication for the chat application backend.

## Features

- User registration
- User login
- JWT-based authentication
- Password hashing
- Token verification

## Setup

1. Clone the repository.
2. Install dependencies:
    ```bash
    pip install -r requirement.txt
    ```
3. Configure environment variables in `.env`.
   ```SECRET_KEY
    DB_NAME
    DB_USERNAME
    DB_PASSWORD
    DB_URL
    DB_PORT```
4. Run the command
    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

## API Endpoints

- `POST api/register/` — Register a new user
- `POST api/login/` — Authenticate user and receive token

## Technologies

- Django
- Postgress
- JWT
