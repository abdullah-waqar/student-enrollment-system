from models.student import Student

def create_student(db, student_data):
    try:
        new_student = Student(
            name=student_data.name,
            department=student_data.department,
            age=student_data.age
        )

        db.add(new_student)
        db.commit()
        db.refresh(new_student)

        return new_student

    except Exception as e:
        db.rollback()
        raise e


def get_all_students(db):
    return db.query(Student).all()


def get_student_by_id(db, student_id):
    return db.query(Student).filter(Student.id == student_id).first()


def update_student(db, student_id, student_data):
    try:
        student = db.query(Student).filter(Student.id == student_id).first()

        if not student:
            return None

        student.name = student_data.name
        student.department = student_data.department
        student.age = student_data.age

        db.commit()
        db.refresh(student)

        return student

    except Exception as e:
        db.rollback()
        raise e


def delete_student(db, student_id):
    try:
        student = db.query(Student).filter(Student.id == student_id).first()

        if not student:
            return None

        db.delete(student)
        db.commit()

        return student

    except Exception as e:
        db.rollback()
        raise e