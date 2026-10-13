from modules.department.schema import Department
departments = [
    Department(id = 1 , name = "Engineering" , description = "Software Development"),
    Department(id = 2 , name = "Human Resources" , description = "Recruitment and Employee Support"),
    Department(id = 3 , name = "Finance" , description = "Budgeting and Finance")
]

def get_departments():
    return departments

def get_dept_by_id(id):
    for dept in departments:
        if dept.id == id:
            return dept
    return f"No department with {id} exists !!"

def create_new_dept(data):
    for dept in departments:
        if dept.id == data.id:
            return "Department already exists"

    departments.append(data)
    return f"Department added successfully ! Department id is : {data.id}"

def update_dept(id , data):
    for dept in departments:
        if dept.id == id:
            if data.id == id:
                dept.name = data.name
                dept.description = data.description
                return dept
            else:
                return "ID could not be updated !!"
    return f"No department exists with id {id}"
    
    
def delete_dept(id):
    for i , dept in enumerate(departments):
        if dept.id == id:
            departments.pop(i)
            return "Department deleted succesfully"
    return f"No department exists with id {id}"

