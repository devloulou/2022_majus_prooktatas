"""
start_date date,
salary integer,
position_id integer,
employee_name text
"""
import datetime

class Employee:
    def __init__(self, employee_name, salary, position, start_date):
        self.name = employee_name
        self.salary = salary
        self.position = position
        self.start_date = start_date

    def get_employee(self):
        return {
            "name": self.name,
            "salary": self.salary,
            "position": self.position,
            "start_date": self.start_date    
                }

if __name__ == '__main__':
    ceo = Employee(employee_name="John Wick", salary=3_000_000, position="CEO", start_date=datetime.datetime(2022, 7, 30))

    print(ceo.get_employee())