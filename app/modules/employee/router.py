from fastapi import APIRouter, HTTPException

from app.modules.employee.schema import EmployeeSchema
from app.modules.employee import service

from app.modules.employee.exceptions import (
    EmployeeNotFoundException,
    EmployeeAlreadyExistsException
)


router = APIRouter()


# Get all employees
@router.get("/")
def list_employees():
    return service.get_all_employees()


# Get employee by ID
@router.get("/{employee_id}")
def get_employee(employee_id: int):
    try:
        return service.get_employee_by_id(employee_id)

    except EmployeeNotFoundException as e:
        raise HTTPException(
            status_code=404,
            detail={
                "error": "EmployeeNotFoundException",
                "message": str(e)
            }
        )


# Add a new employee
@router.post("/", status_code=201)
def add_employee(employee: EmployeeSchema):
    try:
        return service.create_employee(employee)

    except EmployeeAlreadyExistsException as e:
        raise HTTPException(
            status_code=409,
            detail={
                "error": "EmployeeAlreadyExistsException",
                "message": str(e)
            }
        )


# Update an employee
@router.put("/{employee_id}")
def update_employee(
    employee_id: int,
    updated_data: EmployeeSchema
):
    try:
        return service.update_employee(
            employee_id,
            updated_data
        )

    except EmployeeNotFoundException as e:
        raise HTTPException(
            status_code=404,
            detail={
                "error": "EmployeeNotFoundException",
                "message": str(e)
            }
        )


# Delete an employee
@router.delete("/{employee_id}")
def remove_employee(employee_id: int):
    try:
        deleted = service.delete_employee(employee_id)

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