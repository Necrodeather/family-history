# Family History Project

The "Family History" project is a RESTful API for managing family budgets.

## ✨ Features

- JWT authentication with access/refresh tokens
- Asynchronous database interaction
- Database migrations via Alembic
- Environment variable configuration
- Fully containerized solution

## 🛠 Technologies

- **FastAPI** - Web framework
- **SQLAlchemy 2.0** - ORM
- **PostgreSQL** - Primary database
- **Asyncpg** - Asynchronous PostgreSQL driver
- **Alembic** - Migration management
- **Pydantic** - Data validation
- **Docker** - Containerization

## 📋 Requirements

- Docker >= 27.5.1
- Docker Compose >= 2332

## 🚀 Project Setup

1. Rename `.env.example` to `.env`:

    ```bash
    cp .env.example .env
    ```

2. Fill empty fields in `.env`.
    - To generate `SECRET_KEY`, run this command, copy the key, and paste it into `.env`:

    ```bash
    openssl rand -hex 32
    ```

3. Start the project:

    ```bash
    docker compose up --build -d
    ```

## 📚 API Documentation

After launching the project, explore:

- Swagger UI: `/docs`
- ReDoc: `/redoc`

## ⚙ Configuration

Main environment variables:

### Database

| Variable          | Description                                  | Default Value         |
| ----------------- | :------------------------------------------- | :-------------------- |
| POSTGRES_HOST     | Postgres host                                | `database`            |
| POSTGRES_USER     | Postgres user                                | -                     |
| POSTGRES_PASSWORD | Password                                     | -                     |
| POSTGRES_DRIVER   | SqlAlchemy driver for Postgres               | `postgresql+asyncpg`  |
| POSTGRES_PORT     | Postgres port                                | `5432`                |
| POSTGRES_DB       | Postgres database                            | `family_history`      |
| POSTGRES_ECHO     | SqlAlchemy logging                           | `true`                |

### Application

| Variable                        | Description                          | Default Value |
| ------------------------------- | :----------------------------------- | :------------ |
| APP_HOST                        | Application host                     | `backend`     |
| APP_PORT                        | Application port                     | `8000`        |
| APP_DEBUG_RELOAD                | Debug reload                         | `false`       |
| APP_WORKERS                     | Application workers                  | `1`           |
| APP_ACCESS_TOKEN_EXPIRE_MINUTES | Access token expiration (minutes)    | `5`           |
| APP_REFRESH_TOKEN_EXPIRE_MINUTES| Refresh token expiration (minutes)   | `15`          |
| APP_ALGORITHM                   | Hashing algorithm                    | `HS256`       |
| APP_SECRET_KEY                  | Secret Key                           | -             |
