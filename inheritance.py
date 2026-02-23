
class Person:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number

    def display_information(self):
        print(f"Name: {self.name}\nAge: {self.age}")


class Worker(Person):
    def __init__(self, name, age, id_number, salary, position, company):
        super().__init__(name, age, id_number)
        self.salary = salary
        self.position = position
        self.company = company

    def calculate_annual_salary(self):
        print(f"Annual salary: {12 * self.salary + 2000}")


# Usage example
print("Information:\n")

oscar = Person("Oscar", 23, "76893434")
oscar.display_information()
print("ID:", oscar.id_number)

worker = Worker(
    "Bredalis", 
    34, 
    "564g98800", 
    21000,
    "Programmer", 
    "Google"
)
worker.display_information()
worker.calculate_annual_salary()
