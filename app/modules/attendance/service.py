attendance_records = []

def mark_attendance(employee_id,date,check_in):
    
    for record in attendance_records:
        if record["employee_id"] == employee_id and record["date"] == date:
            return {"error": "Attendance already marked for this employee on this date"}
        
    attendance = {
        
        "employee_id": employee_id,
        "date": date,
        "check_in": check_in,
        "check_out":None,
        "status":"present"
    }
    
    attendance_records.append(attendance)
    return attendance

def check_out_employee(employee_id, date, check_out):
    # Find the employee's attendance record for this date
    for attendance in attendance_records:
        if attendance["employee_id"] == employee_id and attendance["date"] == date:

            # Check whether the employee has already checked out
            if attendance["check_out"] is not None:
                return {
                    "error": "Employee has already checked out"
                }

            # Save the checkout time
            attendance["check_out"] = check_out

            return attendance

    # No attendance record was found
    return {
        "error": "Attendance record not found. Employee must check in first."
    }

    
def get_all_attendance():
        return attendance_records
    
def get_attendance_by_employee(employee_id):
    employee_records = []
    
    for attendance in attendance_records:
        if attendance["employee_id"] == employee_id:
            employee_records.append(attendance)
            return employee_records
        
        

def get_attendance_by_date(employee_id, date):
    # Search through all attendance records
    for attendance in attendance_records:

        # Check employee ID and date
        if (
            attendance["employee_id"] == employee_id
            and attendance["date"] == date
        ):
            # Return the matching record
            return attendance

    # Return None if no record is found
    return None

def update_attendance(employee_id, date, check_in, check_out, status):
    # Search for the employee's attendance record
    for attendance in attendance_records:
        if (
            attendance["employee_id"] == employee_id
            and attendance["date"] == date
        ):
            # Update the record's values
            attendance["check_in"] = check_in
            attendance["check_out"] = check_out
            attendance["status"] = status

            # Return the updated record
            return attendance

    # No matching record was found
    return None


def delete_attendance(employee_id, date):
    # Search for the attendance record
    for attendance in attendance_records:
        if (
            attendance["employee_id"] == employee_id
            and attendance["date"] == date
        ):
            # Remove the matching record
            attendance_records.remove(attendance)

            # Confirm which record was deleted
            return {
                "message": "Attendance record deleted successfully",
                "deleted_record": attendance
            }

    # If no matching record exists
    return None


            