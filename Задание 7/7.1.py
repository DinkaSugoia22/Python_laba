class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_name(self):
        print(self.name)

    def display_salary(self):
        print(self.salary)


employee = Employee('Гришаня', 15000)

employee.display_name()
employee.display_salary()