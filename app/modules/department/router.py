from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.modules.department import service
from app.modules.department.schema import DepartmentCreate
from app.database import get_db

router = APIRouter(prefix="/departments", tags=["Departments"])


@router.get("")
def get_departments(db: Session = Depends(get_db)):
    return service.get_departments(db)


@router.get("/{id}")
def get_dept_by_id(id: int, db: Session = Depends(get_db)):
    return service.get_dept_by_id(id, db)


@router.post("")
def create_new_dept(
    data: DepartmentCreate,
    db: Session = Depends(get_db)
):
    return service.create_new_dept(data, db)


@router.put("/{id}")
def update_dept(
    id: int,
    data: DepartmentCreate,
    db: Session = Depends(get_db)
):
    return service.update_dept(id, data, db)


@router.delete("/{id}")
def delete_dept(id: int, db: Session = Depends(get_db)):
    return service.delete_dept(id, db)