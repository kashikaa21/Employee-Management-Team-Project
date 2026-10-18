<<<<<<< Updated upstream
from fastapi import APIRouter, HTTPException

=======
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
>>>>>>> Stashed changes
from app.modules.employee.schema import EmployeeSchema
from app.modules.employee import service

<<<<<<< HEAD
from app.modules.employee.exceptions import (
    EmployeeNotFoundException,
    EmployeeAlreadyExistsException
)

<<<<<<< Updated upstream

router = APIRouter(prefix="/employees", tags=["Employees"])
=======
router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)
>>>>>>> Stashed changes
=======
router = APIRouter()
>>>>>>> main


@router.get("/")
def list_employees(
    db: Session = Depends(get_db)
):
    return service.get_all_employees(db)


@router.get("/{employee_id}")
<<<<<<< Updated upstream
def get_employee(employee_id: int):
    try:
        return service.get_employee_by_id(employee_id)
=======
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    try:
        return service.get_employee_by_id(
            employee_id,
            db
        )
>>>>>>> Stashed changes

    except EmployeeNotFoundException as e:
        raise HTTPException(
            status_code=404,
<<<<<<< Updated upstream
            detail={
                "error": "EmployeeNotFoundException",
                "message": str(e)
            }
=======
            detail=str(e)
>>>>>>> Stashed changes
        )


@router.post("/", status_code=201)
<<<<<<< Updated upstream
def add_employee(employee: EmployeeSchema):
    try:
        return service.create_employee(employee)
=======
def add_employee(
    employee: EmployeeSchema,
    db: Session = Depends(get_db)
):
    try:
        return service.create_employee(
            employee,
            db
        )
>>>>>>> Stashed changes

    except EmployeeAlreadyExistsException as e:
        raise HTTPException(
            status_code=409,
<<<<<<< Updated upstream
            detail={
                "error": "EmployeeAlreadyExistsException",
                "message": str(e)
            }
=======
            detail=str(e)
>>>>>>> Stashed changes
        )


@router.put("/{employee_id}")
def update_employee(
    employee_id: int,
<<<<<<< Updated upstream
    updated_data: EmployeeSchema
=======
    updated_data: EmployeeSchema,
    db: Session = Depends(get_db)
>>>>>>> Stashed changes
):
    try:
        return service.update_employee(
            employee_id,
<<<<<<< Updated upstream
            updated_data
=======
            updated_data,
            db
>>>>>>> Stashed changes
        )

    except EmployeeNotFoundException as e:
        raise HTTPException(
            status_code=404,
<<<<<<< Updated upstream
            detail={
                "error": "EmployeeNotFoundException",
                "message": str(e)
            }
=======
            detail=str(e)
>>>>>>> Stashed changes
        )


@router.delete("/{employee_id}")
<<<<<<< Updated upstream
def remove_employee(employee_id: int):
    try:
        deleted = service.delete_employee(employee_id)
=======
def remove_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    try:
        deleted = service.delete_employee(
            employee_id,
            db
        )
>>>>>>> Stashed changes

        return {
            "message": "Employee deleted",
            "employee": deleted
        }

    except EmployeeNotFoundException as e:
        raise HTTPException(
            status_code=404,
<<<<<<< Updated upstream
            detail={
                "error": "EmployeeNotFoundException",
                "message": str(e)
            }
=======
            detail=str(e)
>>>>>>> Stashed changes
        )