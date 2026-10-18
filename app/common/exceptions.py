# app/common/exceptions.py

class SalaryNotFoundException(Exception):

    def __init__(self, salary_id):
        self.salary_id = salary_id


class DatabaseException(Exception):

    def __init__(self, message):
        self.message = message