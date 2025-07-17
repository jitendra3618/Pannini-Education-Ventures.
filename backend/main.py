from fastapi import FastAPI
from database import Base, engine
import models
from routers import users, assignments, submissions
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"]
)
app.include_router(users.router)
app.include_router(assignments.router)
app.include_router(submissions.router)
