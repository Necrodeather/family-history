# Family History Project

> A RESTful API for managing family budgets, built with FastAPI and a modern Python stack.

This application allows users to track their income and expenses, manage categories, and get an overview of their financial situation. It is fully containerized for easy deployment and development.

## 📋 Table of Contents

- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🚀 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Setup](#installation--setup)
- [📚 API Reference](#-api-reference)
  - [Authentication](#authentication)
  - [Expenses](#expenses)
  - [Expense Categories](#expense-categories)
  - [Income](#income)
  - [Income Categories](#income-categories)
  - [Users](#users)
- [⚙️ Configuration](#️-configuration)
- [📄 License](#-license)

## ✨ Features

- **Authentication:** Secure JWT-based authentication with access and refresh tokens.
- **Asynchronous:** Built with `async` and `await` for high performance.
- **Database Migrations:** Alembic for easy database schema management.
- **Configuration:** Environment variable-based configuration using Pydantic.
- **Containerized:** Docker and Docker Compose for a consistent development and production environment.
- **Caching:** Redis for improved performance and reduced database load.

## 🛠️ Tech Stack

- **Backend:** FastAPI, Python 3.12
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy 2.0 (with `asyncpg`)
- **Migrations:** Alembic
- **Data Validation:** Pydantic
- **Caching:** Redis
- **Containerization:** Docker, Docker Compose

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Docker >= 27.5.1
- Docker Compose >= 2.23.0

### Installation & Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Necrodeather/family-history.git
    cd family-history
    ```

2. **Set up environment variables:**

    Copy the example environment file:

    ```bash
    cp .env.example .env
    ```

    Open the `.env` file and fill in the required variables. To generate a secure `SECRET_KEY`, use the following command:

    ```bash
    openssl rand -hex 32
    ```

3. **Build and run the application:**

    ```bash
    docker compose up --build -d
    ```

    The API will be available at `http://localhost:8000`.

## 📚 API Reference

Once the application is running, you can access the interactive API documentation at:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

### Authentication

- `POST /api/v1/auth/register`: Register a new user.
- `POST /api/v1/auth/login`: Authenticate and receive JWT tokens.
- `POST /api/v1/auth/refresh`: Refresh an access token.
- `GET /api/v1/auth/me`: Get the current authenticated user's information.

### Expenses

- `GET /api/v1/budget/expenses/`: Get a list of expenses.
- `POST /api/v1/budget/expenses/`: Create a new expense.
- `GET /api/v1/budget/expenses/{budget_id}`: Get a specific expense.
- `PUT /api/v1/budget/expenses/{budget_id}`: Update an expense.
- `DELETE /api/v1/budget/expenses/{budget_id}`: Delete an expense.

### Expense Categories

- `GET /api/v1/budget/expenses_category/`: Get a list of expense categories.
- `POST /api/v1/budget/expenses_category/`: Create a new expense category.
- `GET /api/v1/budget/expenses_category/{category_id}`: Get a specific expense category.
- `PUT /api/v1/budget/expenses_category/{category_id}`: Update an expense category.
- `DELETE /api/v1/budget/expenses_category/{category_id}`: Delete an expense category.

### Income

- `GET /api/v1/budget/income/`: Get a list of incomes.
- `POST /api/v1/budget/income/`: Create a new income.
- `GET /api/v1/budget/income/{income_id}`: Get a specific income.
- `PUT /api/v1/budget/income/{income_id}`: Update an income.
- `DELETE /api/v1/budget/income/{income_id}`: Delete an income.

### Income Categories

- `GET /api/v1/budget/incomes_category/`: Get a list of income categories.
- `POST /api/v1/budget/incomes_category/`: Create a new income category.
- `GET /api/v1/budget/incomes_category/{category_id}`: Get a specific income category.
- `PUT /api/v1/budget/incomes_category/{category_id}`: Update an income category.
- `DELETE /api/v1/budget/incomes_category/{category_id}`: Delete an income category.

### Users

- `GET /api/v1/user/`: Get a list of users.
- `GET /api/v1/user/{user_id}`: Get a specific user.

## ⚙️ Configuration

The application is configured using environment variables. See `.env.example` for a complete list of options.

### Database

| Variable          | Description                    | Default Value        |
| ----------------- | ------------------------------ | -------------------- |
| `POSTGRES_HOST`     | Postgres host                  | `database`           |
| `POSTGRES_USER`     | Postgres user                  | -                    |
| `POSTGRES_PASSWORD` | Password                       | -                    |
| `POSTGRES_DRIVER`   | SQLAlchemy driver for Postgres | `postgresql+asyncpg` |
| `POSTGRES_PORT`     | Postgres port                  | `5432`               |
| `POSTGRES_DB`       | Postgres database name         | `family_history`     |
| `POSTGRES_ECHO`     | SQLAlchemy logging             | `true`               |

### Application

| Variable                         | Description                       | Default Value |
| -------------------------------- | --------------------------------- | :------------ |
| `APP_HOST`                         | Application host                  | `backend`     |
| `APP_PORT`                         | Application port                  | `8000`        |
| `APP_DEBUG_RELOAD`                 | Debug reload                      | `false`       |
| `APP_WORKERS`                      | Application workers               | `1`           |
| `APP_ACCESS_TOKEN_EXPIRE_MINUTES`  | Access token expiration (minutes) | `5`           |
| `APP_REFRESH_TOKEN_EXPIRE_MINUTES` | Refresh token expiration (minutes)| `15`          |
| `APP_ALGORITHM`                    | Hashing algorithm                 | `HS256`       |
| `APP_SECRET_KEY`                   | Secret Key                        | -             |

### Redis

| Variable     | Description      | Default Value |
| ------------ | ---------------- | :------------ |
| `REDIS_HOST` | Redis host       | `cache`       |
| `REDIS_PORT` | Redis port       | `6379`        |
| `REDIS_DB`   | Redis database   | `false`       |

## 📄 License

This project is licensed under the **GPL-3.0 License**. See the [LICENSE](LICENSE) file for details.
