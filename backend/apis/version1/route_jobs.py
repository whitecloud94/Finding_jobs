from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from typing import List

from db.session import get_db

from schemas.jobs import JobCreate, ShowJob
from db.repository.jobs import create_new_job, retreive_job, list_jobs

router = APIRouter()

@router.post("/create-job/", response_model=ShowJob)
async def create_user(job : JobCreate, db: Session = Depends(get_db)):
    current_user = 1
    job = create_new_job(job = job, db=db, owner_id=current_user)
    return job

@router.get("/get/{id}", response_model=ShowJob) 
async def read_job(id:int, db:Session = Depends(get_db)):
    job = retreive_job(id=id, db=db)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with this id {id} dose not exist.")
    return job

@router.get("/all",response_model=List[ShowJob])
async def read_jobs(db:Session = Depends(get_db)):
    jobs = list_jobs(db=db)
    return jobs