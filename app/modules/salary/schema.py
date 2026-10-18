from pydantic import BaseModel, Field

class Salary(BaseModel):
    salary_id: int
    employee_id: int

    basic_salary: float = Field(
        gt=0,
        description="Salary must be greater than 0"
    )
    allowances: float
    deductions: float

    class Config:
        from_attributes = True



