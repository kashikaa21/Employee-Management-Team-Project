<<<<<<< Updated upstream
=======
from sqlalchemy.orm import Session

>>>>>>> Stashed changes
from app.modules.employee.schema import EmployeeSchema
from app.modules.employee.model import Employee
from app.modules.employee.exceptions import (
    EmployeeNotFoundException,
    EmployeeAlreadyExistsException
)

<<<<<<< Updated upstream
from app.modules.employee.exceptions import (
    EmployeeNotFoundException,
    EmployeeAlreadyExistsException
)

# employee data
employees = [
    EmployeeSchema(
        employee_id=1,
        name="Isheeta",
        department="IT",
        designation="Developer",
        salary=45000
    ),
    EmployeeSchema(
        employee_id=2,
        name="Garima",
        department="HR",
        designation="HR Manager",
        salary=55000
    ),
    EmployeeSchema(
        employee_id=3,
        name="Ananya",
        department="Finance",
        designation="Accountant",
        salary=50000
    ),
    EmployeeSchema(
        employee_id=4,
        name="Kashika",
        department="Marketing",
        designation="Marketing Specialist",
        salary=48000
=======

def get_all_employees(db: Session):
    return db.query(Employee).all()


def get_employee_by_id(employee_id: int, db: Session):
    employee = (
        db.query(Employee)
        .filter(Employee.employee_id == employee_id)
        .first()
>>>>>>> Stashed changes
    )

    if not employee:
        raise EmployeeNotFoundException(
            f"Employee with ID {employee_id} not found"
        )

<<<<<<< Updated upstream
# Get all employees
def get_all_employees():
    return employees


# Get employee by ID
def get_employee_by_id(employee_id: int):
    for employee in employees:
        if employee.employee_id == employee_id:
            return employee

    raise EmployeeNotFoundException(
        f"Employee with ID {employee_id} not found"
    )


# Add a new employee
def create_employee(employee: EmployeeSchema):
    for existing in employees:
        if existing.employee_id == employee.employee_id:
            raise EmployeeAlreadyExistsException(
                "Employee ID already exists"
            )

    employees.append(employee)
    return employee


# Update an employee
def update_employee(
    employee_id: int,
    updated_data: EmployeeSchema
):
    for index, employee in enumerate(employees):
        if employee.employee_id == employee_id:
            employees[index] = updated_data
            return updated_data

    raise EmployeeNotFoundException(
        f"Employee with ID {employee_id} not found"
    )


# Delete an employee
def delete_employee(employee_id: int):
    for index, employee in enumerate(employees):
        if employee.employee_id == employee_id:
            return employees.pop(index)

    raise EmployeeNotFoundException(
        f"Employee with ID {employee_id} not found"
    )
=======
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

    db.delete(employee)
    db.commit()

    return employee
>>>>>>> Stashed changes
