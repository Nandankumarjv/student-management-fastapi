from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from schemas.student import (
    createStudent,
    updateStudent,
    responseStudent
)
from database.database import get_db
from models.student import Student

router=APIRouter(
    prefix='/students',
    tags=["Students"]
)

@router.post("/",response_model=responseStudent,status_code=status.HTTP_201_CREATED)
def create_student(student:createStudent,db: Session=Depends(get_db)):
    new_student=Student(
        name=student.name,
        age=student.age,
        gender=student.gender
    )
    db.add(new_student)
    try:
        db.commit()
        db.refresh(new_student)
    except Exception:
        db.rollback()
        raise
    return new_student

@router.get("/",response_model=list[responseStudent],status_code=status.HTTP_200_OK)
def get_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students

@router.get("/{Student_id}",response_model=responseStudent,status_code=status.HTTP_200_OK)
def details_byID(student_id:int,db: Session=Depends(get_db)):
    student=db.get(Student,student_id)
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not exist"
        )
    return student

@router.put("/{student_id}",response_model=responseStudent,status_code=status.HTTP_200_OK)
def update_student(student_id:int,student:updateStudent,db: Session=Depends(get_db)):

    db_student=db.get(Student,student_id)
    if db_student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    db_student.name=student.name
    db_student.age=student.age
    db_student.gender=student.gender
    try:
        db.commit()
        db.refresh(db_student)
    except Exception:
        db.rollback()
        raise
    return db_student

@router.delete("/{student_id}",status_code=status.HTTP_204_NO_CONTENT)
def remove_student(student_id:int,db: Session=Depends(get_db)):

    student=db.get(Student,student_id)
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    db.delete(student)
    try:
        db.commit()
    except Exception:
        db.rollback()
        raise

