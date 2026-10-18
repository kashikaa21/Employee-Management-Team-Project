from sqlalchemy.orm import Session

from app.modules.department.model import Department


def get_departments(db: Session):
    return db.query(Department).all()


def get_dept_by_id(id: int, db: Session):

    dept = (
        db.query(Department)
        .filter(Department.id == id)
        .first()
    )

    if not dept:
        return {"message": f"No department with id {id} exists"}

    return dept


def create_new_dept(data, db: Session):

    dept = Department(
        name=data.name,
        description=data.description
    )

    db.add(dept)
    db.commit()
    db.refresh(dept)

    return dept


def update_dept(id: int, data, db: Session):

    dept = (
        db.query(Department)
        .filter(Department.id == id)
        .first()
    )

    if not dept:
        return {"message": f"No department exists with id {id}"}

    dept.name = data.name
    dept.description = data.description

    db.commit()
    db.refresh(dept)

    return dept


def delete_dept(id: int, db: Session):

    dept = (
        db.query(Department)
        .filter(Department.id == id)
        .first()
    )

    if not dept:
        return {"message": f"No department exists with id {id}"}

    db.delete(dept)
    db.commit()

    return {"message": "Department deleted successfully"}

