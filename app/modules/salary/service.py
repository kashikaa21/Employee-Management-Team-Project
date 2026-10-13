
from app.modules.salary.schema import Salary

salaries = [
    Salary(salary_id=1, employee_id=101, basic_salary=45000.0, allowances=5000.0, deductions=2000.0),
    Salary(salary_id=2, employee_id=102, basic_salary=55000.0, allowances=7000.0, deductions=3000.0),
    Salary(salary_id=3, employee_id=103, basic_salary=40000.0, allowances=3500.0, deductions=1500.0)
]

def get_all_salaries():
    return salaries


def get_salary_by_id(salary_id: int):
    for salary in salaries:
        if salary.salary_id == salary_id:
            return salary

    return None


def add_salary(salary: Salary):
    salaries.append(salary)
    return salary



def update_salary(salary_id: int, salary: Salary):
    for i in range(len(salaries)):
        if salaries[i].salary_id == salary_id:
            salaries[i] = salary
            return salary

    return None


def delete_salary(salary_id: int):
    for i in range(len(salaries)):
        if salaries[i].salary_id == salary_id:
            deleted_salary = salaries[i]
            del salaries[i]
            return deleted_salary

    return None

