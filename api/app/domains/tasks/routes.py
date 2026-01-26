from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.domains.tasks.schemas import TaskCreate
from app.domains.tasks.service import TaskRepository

router = APIRouter()

@router.post("/tasks")
def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
    repo = TaskRepository(db)
    return repo.add(task_data.title, task_data.status)

@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    repo = TaskRepository(db)
    return repo.get()

@router.delete("/tasks/{task_id}")
def delete_task(task_id: str, db: Session = Depends(get_db)):
    repo = TaskRepository(db)
    repo.remove(task_id)
