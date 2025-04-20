from fastapi import APIRouter

router = APIRouter()

# In-memory ToDo storage
todos = [
    {"id": 1, "task": "Learn FastAPI", "completed": False},
    {"id": 2, "task": "Build a ToDo App", "completed": True},
    {"id": 3, "task": "Call API from HTML", "completed": False}
]

@router.get("/api/todos")
def get_todos():
    return todos
