# Домашнее задание по теме "Модели SQLALchemy. Отношения между таблицами." Modul 17-3

from fastapi import FastAPI
from app.routers import task
from app.routers import user

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message" : "Welcome to TaskManager"}

app.include_router(task.router)
app.include_router(user.router)


# загрузка    uvicorn main:app
#  alembic revision -m 'initial migration'