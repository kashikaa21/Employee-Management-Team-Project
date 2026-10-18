from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.modules.salary.schema import Salary
from app.modules.salary import service
from app.database import get_db

router = APIRouter()


@router.get("/")
def get_all_salaries(
    db: Session = Depends(get_db)
):
    return service.get_all_salaries(db)


@router.get("/{salary_id}")
def get_salary_by_id(
    salary_id: int,
    db: Session = Depends(get_db)
):
    return service.get_salary_by_id(
        db,
        salary_id
    )


@router.post("/")
def add_salary(
    salary: Salary,
    db: Session = Depends(get_db)
):
    return service.add_salary(
        db,
        salary
    )


@router.put("/{salary_id}")
def update_salary(
    salary_id: int,
    salary: Salary,
    db: Session = Depends(get_db)
):
    updated_salary = service.update_salary(
        db,
        salary_id,
        salary
    )

    if updated_salary is None:
        return {"message": "SalaryId Not Found!!!"}

    return updated_salary


@router.delete("/{salary_id}")
def delete_salary(
    salary_id: int,
    db: Session = Depends(get_db)
):
    deleted_salary = service.delete_salary(
        db,
        salary_id
    )

    if deleted_salary is None:
        return {"message": "Salary Not Found!!!"}

    return deleted_salary




    


