🚀 FastAPI x MySQL - My First Backend API Integration Project
---


![App Screenshot](images/fastapi.jpg)


This project is a milestone in my backend development journey where I built a simple, structured CRUD API using FastAPI and MySQL. The goal was not just to create endpoints — but to understand how backend systems communicate with databases, handle requests, and structure real-world applications.


-----

## 🌿 Features

- User creation with POST request
- Fetching user info via GET endpoint
- SQLAlchemy integration with MySQL
- Pydantic-based data validation
- Async endpoints with FastAPI

  ---
  
## 🧠 What I Learned

1. Over the course of building this project, I dove deep into several core concepts of backend API development:

2. How FastAPI works under the hood: I learned about async functions, dependency injection, route handling, and how FastAPI simplifies request validation and error management using Pydantic models.

3. Database integration with SQLAlchemy ORM: I set up and configured a MySQL database connection using SQLAlchemy and learned how to define models, create tables, and perform queries — all using Python classes.

4. How to handle user data: I implemented endpoints for user creation and retrieval and ensured data consistency by managing sessions and commits.

5. Proper error handling: I learned to gracefully handle edge cases like “User not found” using HTTPException.

6. Project structuring: I understood how to split code into logical files: separating models, database config, and application routes.



----


## 🛠️ Tools & Technologies Used

- FastAPI  – Web framework

-  MySQL  – Relational database

-  SQLAlchemy  – ORM for database interaction

-  Pydantic  – Data validation

-  vicorn  – ASGI server


------


## 🌱 Why This Project Matters

This wasn’t just about writing code — it was about understanding backend architecture. This project taught me how APIs work, how databases talk to Python apps, and how to ensure clean code using best practices.

It’s the foundation for building larger, more complex backend systems — and it gave me the confidence to explore concepts like JWT authentication, file uploads, background tasks, and full-stack integrations later.


------
## 📁 Project Structure

fast_api/

├── main.py           # FastAPI app with endpoints

├── model.py          # SQLAlchemy User model

├── database.py       # DB connection setup

└── requirements.txt  # Python dependencies


---

## 🔌 MySQL Setup

Make sure you have MySQL installed and a database created:

```sql

CREATE DATABASE fastapi_db;
```

Update your database.py connection string like this:

```python

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://username:password@localhost/fastapi_db"
```


-----


## ▶️ Run the Project

1. Install dependencies:

```bash

pip install fastapi uvicorn sqlalchemy mysql-connector-python
```

2. Run the server:

```bash

uvicorn main:app --reload
```

3. Visit Docs:

    1. Swagger UI: http://127.0.0.1:8000/docs

    2. ReDoc: http://127.0.0.1:8000/redoc


  -----
  

## ✅ Endpoints

| Method | Endpoint      | Description       |
| ------ | ------------- | ----------------- |
| POST   | `/users`      | Create a new user |
| GET    | `/users/{id}` | Get user by ID    |

![App Screenshot](images/2.0.jpg)
![App Screenshot](images/sql_tables.jpg)

----

📍 Next Steps

I'm excited to keep growing! Here's what I plan to explore next:

1. Adding authentication using OAuth2 or JWT

2. Creating a frontend (maybe with React or a minimal Streamlit dashboard)

3. Deploying this API on Render, Railway, or AWS

----

💡 Final Thoughts
This project is small, but it’s a meaningful step forward in my AI/ML + backend journey. By combining modern tools like FastAPI with robust databases like MySQL, I now have a clearer picture of how production systems are built — and I’m just getting started.


----

## Author - PriiiAiVerse

## License

This project is licensed under the MIT License -
