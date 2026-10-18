from pydantic import BaseModel, Field


class EmployeeSchema(BaseModel):
    employee_id: int
    name: str
    department: str
    designation: str
    salary: float = Field(gt=0)

    class Config:
        from_attributes = True