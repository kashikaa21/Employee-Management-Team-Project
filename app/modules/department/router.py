from fastapi import APIRouter
from modules.department import service
from modules.department.schema import Department

router = APIRouter()

@router.get("")
def get_departments():
    return service.get_departments()

@router.get("/{id}")
def get_dept_by_id(id:int):
    return service.get_dept_by_id(id)

@router.post("")
def create_new_dept(data : Department):
    return service.create_new_dept(data)

@router.put("/{id}")
def update_dept(id : int , data : Department):
    return service.update_dept(id , data)

@router.delete("/{id}")
def delete_dept(id : int):
    return service.delete_dept(id)
