from models.course import Course

def create_course(db, CourseData):
    try:
        new_course = Course(
            course_name = CourseData.course_name,
            course_code = CourseData.course_code,
            credits = CourseData.credits
        )

        db.add(new_course)
        db.commit()
        db.refresh(new_course)

        return new_course

    except Exception as e:
        db.rollback()
        raise e

def get_all_courses(db):
    return db.query(Course).all()

def get_course_by_id(db, id):
    return db.query(Course).filter(Course.id == id).first()
def delete_course_by_id(db, id):
    try:
        course = db.query(Course).filter(Course.id == id).first()

        if not course:
            return None
        
        db.delete(course)
        db.commit()
        return course
    except Exception as e:
        db.rollback() 
        raise e
    
def update_course(db, id, course_data):
    try:
        course = db.query(Course).filter(Course.id == id).first()

        if not course:
            return None

        # Updating the attributes
        course.course_name = course_data.course_name
        course.course_code = course_data.course_code
        course.credits = course_data.credits

        db.commit()
        db.refresh(course)
        return course
    
    except Exception as e:
        db.rollback() 
        raise e