from sqlalchemy import Column, Integer, String
from core.database import Base

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    course_name = Column(String(100), nullable=False)
    course_code = Column(String(20), nullable=False, unique=True) 
    credits = Column(Integer, nullable=False)