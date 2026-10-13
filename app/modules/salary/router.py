from fastapi import APIRouter
from app.modules.salary.schema import Salary
from app.modules.salary import service

router = APIRouter(prefix="/salaries", tags=["Salary"])


@router.get("/")
def get_all_salaries():
    return service.get_all_salaries()


@router.get("/{salary_id}")
def get_salary_by_id(salary_id: int):
    salary = service.get_salary_by_id(salary_id)
    if salary is None:
        return "SalaryId Not Found!!!"

    return salary


@router.post("/")
def add_salary(salary: Salary):
    return service.add_salary(salary)


@router.put("/{salary_id}")
def update_salary(salary_id: int, salary: Salary):
    updated_salary = service.update_salary(salary_id, salary)
    if updated_salary is None:
        return "SalaryId Not Found!!!"

    return updated_salary


@router.delete("/{salary_id}")
def delete_salary(salary_id: int):
    deleted_salary = service.delete_salary(salary_id)
    if deleted_salary is None:
        return "Salary Not Found!!!"

    return "Salary Deleted Successfully!!"




    


