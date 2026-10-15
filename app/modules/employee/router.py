
from fastapi import APIRouter, HTTPException
from app.modules.employee.schema import EmployeeSchema
from app.modules.employee import service

router = APIRouter()


# Get all employees
@router.get("/")
def list_employees():
    return service.get_all_employees()


# Get employee by ID
@router.get("/{employee_id}")
def get_employee(employee_id: int):
    employee = service.get_employee_by_id(employee_id)

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


# Add a new employee
@router.post("/", status_code=201)
def add_employee(employee: EmployeeSchema):
    created = service.create_employee(employee)

    if created is None:
        raise HTTPException(status_code=409, detail="Employee ID already exists")

    return created


# Update an employee
@router.put("/{employee_id}")
def update_employee(employee_id: int, updated_data: EmployeeSchema):
    updated = service.update_employee(employee_id, updated_data)

    if updated is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return updated


# Delete an employee
@router.delete("/{employee_id}")
def remove_employee(employee_id: int):
    deleted = service.delete_employee(employee_id)

    if deleted is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {"message": "Employee deleted", "employee": deleted}
