from fastapi import FastAPI, HTTPException
from typing import List, Optional

from pydantic import BaseModel
 
app = FastAPI()

todos = []

class Todo(BaseModel):
    id : int
    title : str
    username: str 
    contact : int
    completed: bool

@app.post("/todos/")
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

@app.get("/todos/")
def get_todos():
    return todos

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return updated_todo
    return {"error": "To-do item not found!"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "Todo item deleted!"}
