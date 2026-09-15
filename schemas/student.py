from pydantic import BaseModel, ConfigDict, Field, EmailStr

class createStudent(BaseModel):
    name:str = Field(min_length=3)
    age:int = Field(ge=5,le=24)
    gender:str = Field(min_length=1,max_length=10)    

class updateStudent(BaseModel):
    name:str = Field(min_length=3)
    age:int = Field(ge=5,le=24)
    gender:str = Field(min_length=1,max_length=10)

class responseStudent(BaseModel):
    id:int
    name:str
    age:int
    gender:str

    model_config=ConfigDict(
        from_attributes=True
    )