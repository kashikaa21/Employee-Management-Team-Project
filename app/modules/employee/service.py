from sqlalchemy.orm import Session

from app.modules.employee.schema import EmployeeSchema
from app.modules.employee.model import Employee
from app.modules.employee.exceptions import (
    EmployeeNotFoundException,
    EmployeeAlreadyExistsException
)


def get_all_employees(db: Session):
    return db.query(Employee).all()


def get_employee_by_id(employee_id: int, db: Session):
    employee = (
        db.query(Employee)
        .filter(Employee.employee_id == employee_id)
        .first()
    )

    if not employee:
        raise EmployeeNotFoundException(
            f"Employee with ID {employee_id} not found"
        )

    return employee


def create_employee(employee: EmployeeSchema, db: Session):

    existing = (
        db.query(Employee)
        .filter(Employee.employee_id == employee.employee_id)
        .first()
    )

    if existing:
        raise EmployeeAlreadyExistsException(
            "Employee ID already exists"
        )

    new_employee = Employee(
        employee_id=employee.employee_id,
        name=employee.name,
        department=employee.department,
        designation=employee.designation,
        salary=employee.salary
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee


def update_employee(
    employee_id: int,
    updated_data: EmployeeSchema,
    db: Session
):

    employee = (
        db.query(Employee)
        .filter(Employee.employee_id == employee_id)
        .first()
    )

    if not employee:
        raise EmployeeNotFoundException(
            f"Employee with ID {employee_id} not found"
        )

    employee.name = updated_data.name
    employee.department = updated_data.department
    employee.designation = updated_data.designation
    employee.salary = updated_data.salary

    db.commit()
    db.refresh(employee)

    return employee


def delete_employee(employee_id: int, db: Session):

    employee = (
        db.query(Employee)
        .filter(Employee.employee_id == employee_id)
        .first()
    )

    if not employee:
        raise EmployeeNotFoundException(
            f"Employee with ID {employee_id} not found"
        )


