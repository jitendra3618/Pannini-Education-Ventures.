from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str

class UserLogin(BaseModel):
    email: str
    password: str

class AssignmentCreate(BaseModel):
    title: str
    description: str
    due_date: str

class SubmissionCreate(BaseModel):
    content: str
