""" ЗаданиеНеобходимо создать API для управления списком задач. Каждая задача должна содержать заголовок и описание. Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).
API должен содержать следующие конечные точки:
— GET /tasks — возвращает список всех задач.
— GET /tasks/{id} — возвращает задачу с указанным идентификатором.
— POST /tasks — добавляет новую задачу.
— PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
— DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.
Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа. Для этого использовать библиотеку Pydantic. """

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Модель данных для задачи
class Task(BaseModel):
    title: str
    description: str
    status: bool

tasks = []

# Конечная точка для получения списка всех задач
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

# Конечная точка для получения задачи по id
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return tasks[task_id]

# Конечная точка для добавления новой задачи
@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task

# Конечная точка для обновления задачи по id
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Задача не найдена")
    tasks[task_id] = updated_task
    return updated_task

# Конечная точка для удаления задачи по id
@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Задача не найдена")
    deleted_task = tasks.pop(task_id)
    return deleted_task
