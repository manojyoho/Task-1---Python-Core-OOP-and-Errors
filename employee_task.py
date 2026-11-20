employees = [
    {"id": 1, "name": "Arun", "department": "Sales", "salary": 30000, "city": "Chennai"},
    {"id": 2, "name": "Priya", "department": "HR", "salary": 45000, "city": "Chennai"},
    {"id": 3, "name": "Rahul", "department": "IT", "salary": 60000, "city": "Bangalore"},
    {"id": 4, "name": "Divya", "department": "IT", "salary": 75000, "city": "Chennai"},
    {"id": 5, "name": "Karthik", "department": "Finance", "salary": 90000, "city": "Mumbai"},
    {"id": 6, "name": "Meena", "department": "Sales", "salary": 52000, "city": "Bangalore"},
    {"id": 7, "name": "Suresh", "department": "IT", "salary": 68000, "city": "Chennai"},
    {"id": 8, "name": "Anitha", "department": "HR", "salary": 48000, "city": "Mumbai"},
]

def bonus(salary, rate=0.1, *extras, **options):
    total = salary * rate + sum(extras)
    if "cap" in options:
        total = min(total, options["cap"])
    return total


class InvalidSalaryError(ValueError):
    pass

class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return f"{super().get_details()}, Team size: {self.team_size}"


above_50000 = [employee["name"] for employee in employees if employee["salary"] > 50000]
raised_salaries = list(map(lambda employee: employee["salary"] * 1.1, employees))
chennai_employees = list(filter(lambda employee: employee["city"] == "Chennai", employees))

print(f"Above 50000: {above_50000}")
print(f"Chennai: {[employee['name'] for employee in chennai_employees]}")

for salary in [0] + [employee["salary"] for employee in employees]:
    if salary == 0:
        continue
    if salary > 85000:
        break

try:
    Employee("Invalid", -500)
except InvalidSalaryError as error:
    print(f"Error: {error}")
finally:
    print("Transaction finished.")
