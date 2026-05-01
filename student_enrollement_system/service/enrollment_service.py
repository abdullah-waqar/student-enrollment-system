from models.enrollment import Enrollment
from sqlalchemy.orm import Session
from models.course import Course

def enroll_student_in_course(db, student_id: int, course_id: int):
    # 1. Create the link
    new_enrollment = Enrollment(student_id=student_id, course_id=course_id)
    
    # 2. Save to database
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)
    
    return new_enrollment

def get_courses_by_student(db: Session, student_id: int):
    return db.query(Course).join(Enrollment).filter(Enrollment.student_id == student_id).all()

def get_students_by_course(db: Session, course_id: int):
    from models.student import Student # Local import to avoid circular dependency
    return db.query(Student).join(Enrollment).filter(Enrollment.course_id == course_id).all()