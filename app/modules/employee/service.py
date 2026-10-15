
from app.modules.employee.schema import EmployeeSchema

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
    )
]


# Get all employees
def get_all_employees():
    return employees


# Get employee by ID
def get_employee_by_id(employee_id: int):
    for employee in employees:
        if employee.employee_id == employee_id:
            return employee
    return None


# Add a new employee
def create_employee(employee: EmployeeSchema):
    for existing in employees:
        if existing.employee_id == employee.employee_id:
            return None

    employees.append(employee)
    return employee


# Update an employee
def update_employee(employee_id: int, updated_data: EmployeeSchema):
    for index, employee in enumerate(employees):
        if employee.employee_id == employee_id:
            employees[index] = updated_data
            return updated_data
    return None


# Delete an employee
def delete_employee(employee_id: int):
    for index, employee in enumerate(employees):
        if employee.employee_id == employee_id:
            return employees.pop(index)
    return None
