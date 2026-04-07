from pydantic import BaseModel

# For creating task
class TaskCreate(BaseModel):
    title: str
    description: str

# For returning task
class Task(TaskCreate):
    id: int

    class Config:
        orm_mode = True