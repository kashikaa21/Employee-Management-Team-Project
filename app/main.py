from fastapi import FastAPI
from modules.department import router as department_route

app = FastAPI()

app.include_router(
    department_route.router ,
    prefix = "/department",
    tags = ["Department Management"])