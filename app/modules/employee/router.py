from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.employee.schema import EmployeeSchema
from app.modules.employee import service

from app.modules.employee.exceptions import (
    EmployeeNotFoundException,
    EmployeeAlreadyExistsException
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.get("/")
def list_employees(
    db: Session = Depends(get_db)
):
    return service.get_all_employees(db)


@router.get("/{employee_id}")
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    try:
        return service.get_employee_by_id(
            employee_id,
            db
        )

    except EmployeeNotFoundException as e:
        raise HTTPException(
            status_code=404,
            detail={
                "error": "EmployeeNotFoundException",
                "message": str(e)
            }
        )


@router.post("/", status_code=201)
def add_employee(
    employee: EmployeeSchema,
    db: Session = Depends(get_db)
):
    try:
        return service.create_employee(
            employee,
            db
        )

    except EmployeeAlreadyExistsException as e:
        raise HTTPException(
            status_code=409,
            detail={
                "error": "EmployeeAlreadyExistsException",
                "message": str(e)
            }
        )


@router.put("/{employee_id}")
def update_employee(
    employee_id: int,
    updated_data: EmployeeSchema,
    db: Session = Depends(get_db)
):
    try:
        return service.update_employee(
            employee_id,
            updated_data,
            db
        )

    except EmployeeNotFoundException as e:
        raise HTTPException(
            status_code=404,
            detail={
                "error": "EmployeeNotFoundException",
                "message": str(e)
            }
        )


@router.delete("/{employee_id}")
def remove_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    try:
        deleted = service.delete_employee(
            employee_id,
            db
        )

        return {
            "message": "Employee deleted",
            "employee": deleted
        }

    except EmployeeNotFoundException as e:
        raise HTTPException(
            status_code=404,
            detail={
                "error": "EmployeeNotFoundException",
                "message": str(e)
            }
        )