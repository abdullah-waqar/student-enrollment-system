from pydantic import BaseModel

# What the user sends us (The Request)
class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int

# What we send back to the user (The Response)
class EnrollmentResponse(BaseModel):
    id: int
    student_id: int
    course_id: int

    class Config:
        from_attributes = True