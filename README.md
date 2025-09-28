# CarsAPI

This project is a RESTful API built with **FastAPI**, **SQLAlchemy**, and **Alembic** for database migrations.
It provides endpoints to create, list, update, and delete cars.

---

## Requirements

* Python 3.10+
* Virtual environment (recommended: `venv`)

---

### 1. Clone the Repository

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Database Setup

### 1. Run Migrations with Alembic

Make sure the database exists, then run:

```bash
alembic upgrade head
```

---

## Running the Application

```bash
cd cars_api
fastapi dev app.py
```