from app.modules.salary.schema import Salary
from sqlalchemy.orm import Session
from app.modules.salary.model import SalaryModel

from app.common.exception_handler import SalaryNotFoundException


def get_all_salaries(db: Session):

    return db.query(SalaryModel).all()


def get_salary_by_id(db: Session, salary_id: int):

    salary = (
        db.query(SalaryModel)
        .filter(SalaryModel.salary_id == salary_id)
        .first()
    )

    if not salary:
        raise SalaryNotFoundException(salary_id)

    return salary


def add_salary(db: Session, salary: Salary):

    new_salary = SalaryModel(
        employee_id=salary.employee_id,
        basic_salary=salary.basic_salary,
        allowances=salary.allowances,
        deductions=salary.deductions
    )

    db.add(new_salary)
    db.commit()
    db.refresh(new_salary)

    return new_salary


def update_salary(db: Session,salary_id: int, salary_data: Salary):

    salary = (
        db.query(SalaryModel)
        .filter(SalaryModel.salary_id == salary_id)
        .first()
    )

    if not salary:
        raise SalaryNotFoundException(salary_id)

    salary.employee_id = salary_data.employee_id
    salary.basic_salary = salary_data.basic_salary
    salary.allowances = salary_data.allowances
    salary.deductions = salary_data.deductions

    db.commit()
    db.refresh(salary)

    return salary


def delete_salary(db: Session, salary_id: int):

    salary = (
        db.query(SalaryModel)
        .filter(SalaryModel.salary_id == salary_id)
        .first()
    )

    if not salary:
        raise SalaryNotFoundException(salary_id)

    db.delete(salary)
    db.commit()

    return {
        "message": "Salary Deleted Successfully"
    }