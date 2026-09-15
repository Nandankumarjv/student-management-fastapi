from sqlalchemy import String, Integer, Column
from database.database import Base

class Student(Base):
    __tablename__="students"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50),nullable=False)
    age=Column(Integer)
    gender=Column(String(5))