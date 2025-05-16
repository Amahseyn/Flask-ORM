# Flask-ORM Application

A Flask-based RESTful API with a Django-style ORM (SQLAlchemy), JWT authentication, and PostgreSQL database. The application provides endpoints for managing users, comments, posts, and orders, designed for developers to easily modify and extend.

## Features
- **ORM**: SQLAlchemy with Flask-Migrate for Django-like database migrations.
- **Authentication**: JWT-based authentication for secure access to protected routes.
- **Database**: PostgreSQL for reliable data storage.
- **API Endpoints**:
  - `/users`: User registration, login, and profile management.
  - `/comments`: Create, read, update, and delete comments.
  - `/posts`: Manage posts (e.g., blog or content posts).
  - `/orders`: Handle order creation and management.
- **Modular Structure**: Organized into models and routes for scalability.

## Prerequisites
- Python 3.8+
- PostgreSQL 12+
- Git

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Amahseyn/Flask-ORM.git
   cd Flask-ORM
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://username:password@localhost:5432/flask_orm_db
   SECRET_KEY=your_jwt_secret_key
   ```
   Replace `username`, `password`, and `flask_orm_db` with your PostgreSQL credentials and database name.

5. **Set Up the Database**
   - Create a PostgreSQL database:
     ```bash
     createdb flask_orm_db
     ```
   - Apply migrations:
     ```bash
     flask db upgrade
     ```

6. **Run the Application**
   ```bash
   flask run
   ```
   The API will be available at `http://localhost:5000`.

## API Endpoints

| Endpoint       | Methods         | Description                     |
|----------------|-----------------|---------------------------------|
| `/users`       | GET, POST, PUT, DELETE | Manage user accounts           |
| `/comments`    | GET, POST, PUT, DELETE | Manage comments                |
| `/posts`       | GET, POST, PUT, DELETE | Manage posts                   |
| `/orders`      | GET, POST, PUT, DELETE | Manage orders                  |

- **Authentication**: Protected routes require a JWT token in the `Authorization` header (e.g., `Bearer <token>`).
- Example: `curl -H "Authorization: Bearer <token>" http://localhost:5000/users`

## Project Structure
```
Flask-ORM/
├── app/
│   ├── users/
│   │   ├── models.py    # User model (SQLAlchemy)
│   │   └── routes.py    # User API routes
│   ├── comments/
│   │   ├── models.py    # Comment model (SQLAlchemy)
│   │   └── routes.py    # Comment API routes
│   ├── posts/
│   │   ├── models.py    # Post model (SQLAlchemy)
│   │   └── routes.py    # Post API routes
│   ├── orders/
│   │   ├── models.py    # Order model (SQLAlchemy)
│   │   └── routes.py    # Order API routes
│   ├── __init__.py      # Flask app, SQLAlchemy, and JWT initialization
│   └── config.py        # Configuration settings
├── migrations/          # Database migration files
├── .env                # Environment variables (not tracked)
├── .gitignore          # Git ignore file
├── requirements.txt     # Python dependencies
├── README.md            # This file
└── run.py               # Entry point to run the app
```

## Contributing
To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit changes (`git commit -m "Add YourFeature"`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License.

## Contact
For questions or feedback, contact [Amahseyn](https://github.com/Amahseyn).
