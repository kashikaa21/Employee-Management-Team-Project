from app.modules.attendance.service import mark_attendance , get_all_attendance , check_out_employee , get_attendance_by_employee , get_attendance_by_date , update_attendance , delete_attendance
from fastapi import APIRouter, HTTPException
router = APIRouter()
@router.get("/")
def read_attendance():
    return get_all_attendance

@router.post("/check-in")
def check_in(employee_id : int , date : str , check_in: str):
    return mark_attendance(employee_id , date , check_in)

@router.post("/check-out")
def check_out(employee_id: int, date: str, check_out: str):
    return check_out_employee(employee_id, date, check_out)

@router.get("/employee/{employee_id}")
def read_employee_attendance(employee_id: int):
    return get_attendance_by_employee(employee_id)


@router.get("/{employee_id}/{date}")
def read_attendance_by_date(employee_id: int, date: str):
    attendance = get_attendance_by_date(employee_id, date)

    if attendance is None:
        raise HTTPException(
            status_code=404,
            detail="Attendance record not found"
        )

    return attendance


@router.put("/{employee_id}/{date}")
def update_attendance_record(
    employee_id: int,
    date: str,
    check_in: str,
    check_out: str,
    status: str
):
    attendance = update_attendance(
        employee_id,
        date,
        check_in,
        check_out,
        status
    )

    if attendance is None:
        raise HTTPException(
            status_code=404,
            detail="Attendance record not found"
        )

    return attendance


@router.delete("/{employee_id}/{date}")
def delete_attendance_record(employee_id: int, date: str):
    attendance = delete_attendance(employee_id, date)

    if attendance is None:
        raise HTTPException(
            status_code=404,
            detail="Attendance record not found"
        )

    return attendance






