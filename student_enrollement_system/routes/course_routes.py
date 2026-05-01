from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from utils.helpers import get_db

from service.course_service import (
    get_all_courses, 
    get_course_by_id, 
    create_course,
    update_course,
    delete_course_by_id
)

from schemas.course import CourseCreate, CourseResponse

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.get("/")
def list_all_courses(db: Session = Depends(get_db)):
    return get_all_courses(db)

@router.post("/", response_model=CourseResponse)
def create_new_course(courseData: CourseCreate, db: Session = Depends(get_db)):
    new_course = create_course(db, CourseData=courseData)
    return new_course

@router.get("/{id}", response_model=CourseResponse) 
def read_course(id: int, db: Session = Depends(get_db)):
    course = get_course_by_id(db=db, id=id)

    if not course:
        raise HTTPException(status_code=404, detail="Course does not exist")

    return course

@router.put("/{id}", response_model=CourseResponse)
def update_existing_course(id: int, courseData: CourseCreate, db: Session = Depends(get_db)):
    updated_course = update_course(db, id=id, course_data=courseData)

    if not updated_course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return updated_course

@router.delete("/{id}")
def delete_existing_course(id: int, db: Session = Depends(get_db)):
    result = delete_course_by_id(db, id=id)

    if not result:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return {"message": f"Course {id} deleted successfully"}