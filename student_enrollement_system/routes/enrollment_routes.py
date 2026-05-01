from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.helpers import get_db
from service.enrollment_service import enroll_student_in_course
from service.enrollment_service import get_courses_by_student, get_students_by_course
from schemas.enrollment import EnrollmentCreate, EnrollmentResponse


from schemas.course import CourseResponse
from schemas.student import StudentResponse
from typing import List

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])




@router.post("/", response_model=EnrollmentResponse)
def enroll_student(enrollData: EnrollmentCreate, db: Session = Depends(get_db)):
    return enroll_student_in_course(db, student_id=enrollData.student_id, course_id=enrollData.course_id)


@router.get("/student/{student_id}/courses", response_model=List[CourseResponse])
def list_student_courses(student_id: int, db: Session = Depends(get_db)):
    courses = get_courses_by_student(db, student_id)
    
    return courses

@router.get("/course/{course_id}/students", response_model=List[StudentResponse])
def list_course_students(course_id: int, db: Session = Depends(get_db)):
    students = get_students_by_course(db, course_id)
    return students