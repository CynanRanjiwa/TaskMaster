# SERVE AS THE ENTRY POINT FOR MY FASTAPI APPLICATION
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.connection import engine, get_db
from app.models import Base, User, Task, Category
from app.schemas import UserCreate, TaskCreate, CategoryCreate, UserResponse, TaskResponse, CategoryResponse
app = FastAPI()
# create the databse tables if they don't exist
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(username=user.username, email=user.email, hashed_password=user.hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/tasks/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(title=task.title, description=task.description, due_date=task.due_date,
                   priority=task.priority, status=task.status, owner_id=task.owner_id, category_id=task.category_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

# Add similar endpoints for Category CRUD operations and other necessary functionalities.

"""
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, User, Task, Category
from schemas import TaskCreate, TaskRead, TaskUpdate
import crud

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/tasks/", response_model=TaskRead)
def create_task(task: TaskCreate, db: Session = Depends(SessionLocal)):
    return crud.create_task(db=db, task=task)

@app.get("/tasks/", response_model=List[TaskRead])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(SessionLocal)):
    return crud.get_tasks(db=db, skip=skip, limit=limit)

"""