from fastapi import FastAPI
from core.database import engine, Base

# Import all your routers
from routes import student_routes, course_routes, enrollment_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Enrollment System",
    description="An API to manage students, courses, and enrollments",
    version="1.0.0"
)

app.include_router(student_routes.router)
app.include_router(course_routes.router)
app.include_router(enrollment_routes.router)


@app.get("/")
def root():
    return {"message": "Welcome to the Student Enrollment System API. Go to /docs for the interactive UI!"}