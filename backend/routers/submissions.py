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

@router.post("/assignments/{assignment_id}/submit")
def submit_assignment(assignment_id: int, submission: schemas.SubmissionCreate, user_id: int = Header(...), role: str = Header(...), db: Session = Depends(get_db)):
    if role != "student":
        raise HTTPException(status_code=403, detail="Only students can submit")
    db_submission = models.Submission(assignment_id=assignment_id, student_id=user_id, content=submission.content)
    db.add(db_submission)
    db.commit()
    return {"msg": "Submission successful"}

@router.get("/assignments/{assignment_id}/submissions")
def get_submissions(assignment_id: int, role: str = Header(...), db: Session = Depends(get_db)):
    if role != "teacher":
        raise HTTPException(status_code=403, detail="Only teachers can view submissions")
    return db.query(models.Submission).filter(models.Submission.assignment_id == assignment_id).all()
