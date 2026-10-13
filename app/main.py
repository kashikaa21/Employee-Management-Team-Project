from fastapi import FastAPI
from app.modules.attendance.router import router as attendance_router


app = FastAPI()

app.include_router(attendance_router , prefix="/attendance" , tags=["Attendance"])
