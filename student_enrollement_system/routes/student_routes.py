from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.database import SessionLocal
from service.student_service import get_all_students, get_student_by_id, update_student, delete_student, create_student

from schemas.student import StudentCreate , StudentResponse

from utils.helpers import get_db

router = APIRouter(prefix="/students", tags=["Students"])





@router.get("/")
def list_all_students(db: Session = Depends(get_db)):
    return get_all_students(db)

@router.post("/", response_model=StudentResponse)
def create_new_student(studentData: StudentCreate, db: Session = Depends(get_db)):
    new_student = create_student(db, student_data=studentData)
    
    return new_student

@router.get("/{id}")
def getStudentById(id: int, db: Session = Depends(get_db)):
    
    student = get_student_by_id(db, id) 

    if student is None:
        raise HTTPException(status_code=404, detail="Student Not Found")
    
    return student

@router.put("/{id}")
def updateStudent(id: int, studentData: StudentCreate ,db: Session = Depends(get_db)):
    updated_result = update_student(db, id, student_data=studentData)

    if not updated_result:
        raise HTTPException(status_code=404, detail="Student Not Found")
    
    return updated_result

@router.delete("/{id}")
def deleteStudent(id: int, db: Session = Depends(get_db)):
    result = delete_student(db, id)

    if not result:
        raise HTTPException(status_code=404, detail="Student Not Found")
    
    return result