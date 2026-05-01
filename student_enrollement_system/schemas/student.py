from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    department: str
    age: int

class StudentResponse(BaseModel):
    id: int
    name: str
    department: str
    age: int

    class Config:
        from_attributes = True