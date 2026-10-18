from sqlalchemy import Column, Integer, Float
from app.database import Base


class SalaryModel(Base):

    __tablename__ = "salaries"

    salary_id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(Integer,nullable=False)

    basic_salary = Column(Float, nullable=False)

    allowances = Column(Float, nullable=False)

    deductions = Column(Float, nullable=False)

    