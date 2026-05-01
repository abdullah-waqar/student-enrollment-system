# 🎓 Student Enrollment System

A comprehensive RESTful API for managing student enrollments, built with modern Python technologies. This system allows you to manage students, courses, and enrollment records efficiently.

![FastAPI](https://img.shields.io/badge/FastAPI-v0.100+-green?style=flat-square&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-red?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## ✨ Features

- **Student Management** - Create, read, update, and delete student records
- **Course Management** - Manage course information and details
- **Enrollment System** - Handle student-course enrollments with validation
- **Interactive API Documentation** - Auto-generated Swagger UI and ReDoc documentation
- **Data Validation** - Built-in request/response validation with Pydantic
- **Database ORM** - SQLAlchemy for reliable database interactions
- **Environment Configuration** - Secure configuration management with `.env`

---

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|-----------|---------|---------|
| **FastAPI** | 0.100+ | Web framework for building APIs |
| **Uvicorn** | Latest | ASGI server |
| **SQLAlchemy** | 2.0+ | ORM and database toolkit |
| **Pydantic** | Latest | Data validation and parsing |
| **PostgreSQL** | 12+ | Relational database |
| **Python-dotenv** | Latest | Environment variable management |

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.10 or higher
- PostgreSQL 12 or higher
- pip (Python package manager)
- Git

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/abdullah-waqar/student-enrollment-system.git
cd database_project
```

### 2. Create a Virtual Environment

```bash
# On Windows
python -m venv .venv
.venv\Scripts\Activate.ps1

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r student_enrollement_system/requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
# Database Configuration
DATABASE_URL=postgresql://username:password@localhost:5432/student_enrollment_db

# Optional: Application settings
APP_NAME=Student Enrollment System
APP_VERSION=1.0.0
```

### 5. Initialize the Database

```bash
cd student_enrollement_system
python -c "from core.database import engine, Base; Base.metadata.create_all(bind=engine)"
```

---

## 📁 Project Structure

```
student_enrollement_system/
├── main.py                      # Application entry point
├── requirements.txt             # Project dependencies
│
├── core/
│   ├── config.py               # Configuration management
│   └── database.py             # Database setup and session management
│
├── models/                      # SQLAlchemy ORM models
│   ├── student.py              # Student model
│   ├── course.py               # Course model
│   └── enrollment.py           # Enrollment model
│
├── routes/                      # API route handlers
│   ├── student_routes.py       # Student endpoints
│   ├── course_routes.py        # Course endpoints
│   └── enrollment_routes.py    # Enrollment endpoints
│
├── schemas/                     # Pydantic data validation schemas
│   ├── student.py              # Student request/response schemas
│   ├── course.py               # Course request/response schemas
│   └── enrollment.py           # Enrollment request/response schemas
│
├── service/                     # Business logic layer
│   ├── student_service.py      # Student service logic
│   ├── course_service.py       # Course service logic
│   └── enrollment_service.py   # Enrollment service logic
│
└── utils/
    └── helpers.py              # Utility functions
```

---

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://user:pass@localhost:5432/db` |

### Database Setup

The application automatically creates tables on startup. If you need to reset the database:

```bash
cd student_enrollement_system
python
>>> from core.database import engine, Base
>>> Base.metadata.drop_all(bind=engine)
>>> Base.metadata.create_all(bind=engine)
```

---

## 🏃 Running the Application

### Development Mode

```bash
cd student_enrollement_system
fastapi dev main.py
```

The API will be available at `http://localhost:8000`

### Production Mode

```bash
cd student_enrollement_system
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 📚 API Documentation

Once the server is running, access the interactive documentation:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🔌 API Endpoints

### Students
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/students` | List all students |
| GET | `/students/{id}` | Get student by ID |
| POST | `/students` | Create a new student |
| PUT | `/students/{id}` | Update student |
| DELETE | `/students/{id}` | Delete student |

### Courses
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/courses` | List all courses |
| GET | `/courses/{id}` | Get course by ID |
| POST | `/courses` | Create a new course |
| PUT | `/courses/{id}` | Update course |
| DELETE | `/courses/{id}` | Delete course |

### Enrollments
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/enrollments` | List all enrollments |
| GET | `/enrollments/{id}` | Get enrollment by ID |
| POST | `/enrollments` | Enroll student in course |
| PUT | `/enrollments/{id}` | Update enrollment |
| DELETE | `/enrollments/{id}` | Delete enrollment |

---

## 💡 Usage Examples

### Create a Student

```bash
curl -X POST "http://localhost:8000/students" \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "student_id": "STU001"
  }'
```

### Create a Course

```bash
curl -X POST "http://localhost:8000/courses" \
  -H "Content-Type: application/json" \
  -d '{
    "course_name": "Data Structures",
    "course_code": "CS101",
    "credits": 3
  }'
```

### Enroll Student in Course

```bash
curl -X POST "http://localhost:8000/enrollments" \
  -H "Content-Type: application/json" \
  -d '{
    "student_id": 1,
    "course_id": 1,
    "enrollment_date": "2024-01-15"
  }'
```

---

## 📦 Dependencies

```
fastapi        # Web framework
uvicorn        # ASGI server
sqlalchemy     # ORM
python-dotenv  # Environment variables
pydantic       # Data validation
```

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## 🔐 Security Notes

- Never commit `.env` files with sensitive information
- Use strong database passwords in production
- Implement authentication/authorization for production use
- Validate and sanitize all user inputs (Pydantic handles this)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**Abdullah Waqar**
- GitHub: [@abdullah-waqar](https://github.com/abdullah-waqar)

---

## 📞 Support

For questions or issues, please open an issue on the [GitHub repository](https://github.com/abdullah-waqar/student-enrollment-system/issues).

---

## 🎯 Roadmap

- [ ] Add authentication (JWT)
- [ ] Add authorization (Role-based access)
- [ ] Implement pagination for list endpoints
- [ ] Add filtering and sorting capabilities
- [ ] Unit and integration tests
- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] API rate limiting

---

**Made with ❤️ by Abdullah Waqar**
