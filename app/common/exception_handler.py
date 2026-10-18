from fastapi import Request
from fastapi.responses import JSONResponse

from app.common.exception_handler import (
    SalaryNotFoundException,
    DatabaseException
)


async def salary_not_found_handler(
        request: Request,
        exc: SalaryNotFoundException):

    return JSONResponse(
        status_code=404,
        content={
            "message":
            f"Salary with id {exc.salary_id} not found"
        }
    )


async def database_exception_handler(
        request: Request,
        exc: DatabaseException):

    return JSONResponse(
        status_code=500,
        content={
            "message": exc.message
        }
    )