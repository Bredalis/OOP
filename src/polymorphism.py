
class Employee:
    def __init__(self, name, monthly_salary, bonus_percentage, job_title):
        self.name = name
        self.monthly_salary = monthly_salary
        self.bonus_percentage = bonus_percentage
        self.job_title = job_title

    def calculate_annual_salary(self):
        annual_salary = (
            12 * self.monthly_salary * (1 + self.bonus_percentage / 100)
        )
        print(
            f"The annual salary of {self.job_title} {self.name} "
            f"is {annual_salary:.2f}"
        )


class Accountant(Employee):
    def __init__(
        self, 
        name, 
        monthly_salary, 
        bonus_percentage, 
        job_title="accountant"
    ):
        super().__init__(name, monthly_salary, bonus_percentage, job_title)


class Publicist(Employee):
    def __init__(
        self, 
        name, 
        monthly_salary, 
        bonus_percentage, 
        job_title="publicist"
    ):
        super().__init__(name, monthly_salary, bonus_percentage, job_title)


employees = [
    Employee("Juan", 1000, 1, "employee"),
    Accountant("Juana", 2000, 4),
    Publicist("Lucas", 1200, 5),
]

for employee in employees:
    employee.calculate_annual_salary()
