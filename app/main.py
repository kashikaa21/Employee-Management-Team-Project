from fastapi import FastAPI
from app.modules.attendance.router import router as attendance_router
from app.modules.department.router import router as department_router
from app.modules.employee.router import router as employee_router
from app.modules.salary.router import router as salary_router

from app.database import Base, engine
from app.modules.salary.model import SalaryModel



app = FastAPI(
    title="Employee Management System",
    description="API for Attendance, Department, Employee Details, and Salary Records",
    version="1.0.0"
)

from app.common.exceptions import (
    SalaryNotFoundException,
    DatabaseException
)

from .common.exception_handler import (
    salary_not_found_handler,
    database_exception_handler
)



app.include_router(
    attendance_router,
    prefix="/attendance",
    tags=["Attendance"]
)



app.include_router(
    department_router,
    prefix="/department",
    tags=["Department Management"]
)


app.include_router(
    employee_router,
    prefix="/employee",
    tags=["Employee Details"]
)

app.include_router(
    salary_router,
    prefix="/salary",
    tags=["Salary Records"]
)
Base.metadata.create_all(bind=engine)