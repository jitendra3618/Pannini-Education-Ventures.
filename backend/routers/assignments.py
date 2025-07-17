from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/assignments")
def create_assignment(data: schemas.AssignmentCreate, user_id: int = Header(...), role: str = Header(...), db: Session = Depends(get_db)):
    if role != "teacher":
        raise HTTPException(status_code=403, detail="Only teachers can create assignments")
    assignment = models.Assignment(**data.dict(), created_by=user_id)
    db.add(assignment)
    db.commit()
    return {"msg": "Assignment created"}

@router.get("/assignments")
def list_assignments(db: Session = Depends(get_db)):
    return db.query(models.Assignment).all()
