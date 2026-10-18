from pydantic import BaseModel
class DepartmentCreate(BaseModel):
    name : str
    description : str | None = None

class Department(BaseModel):
    id : int
    name : str
    description : str | None = None
    class Config:
        from_attributes = True