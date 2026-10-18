from pydantic import BaseModel
class Salary(BaseModel):
    salary_id: int 
    employee_id: int 
    basic_salary:float
    allowances: float
    deductions: float