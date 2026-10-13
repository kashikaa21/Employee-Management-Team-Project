from fastapi import FastAPI

# Attendance module
from app.modules.attendance.router import router as attendance_router

# Department module
from app.modules.department import router as department_router

# Employee Details module
# Update this import to match your actual employee router file
from app.modules.employee.router import router as employee_router

# Salary Records module
# Update this import to match your actual salary router file
from app.modules.salary.router import router as salary_router


# Create one FastAPI application
app = FastAPI(
    title="Employee Management System",
    description="API for Attendance, Department, Employee Details, and Salary Records",
    version="1.0.0"
)


# Register Attendance routes
app.include_router(
    attendance_router,
    prefix="/attendance",
    tags=["Attendance"]
)


# Register Department routes
app.include_router(
    department_router.router,
    prefix="/department",
    tags=["Department Management"]
)


# Register Employee Details routes
app.include_router(
    employee_router,
    prefix="/employee",
    tags=["Employee Details"]
)


# Register Salary Records routes
app.include_router(
    salary_router,
    prefix="/salary",
    tags=["Salary Records"]
)

